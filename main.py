import os
import sys
import io
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from bs4 import BeautifulSoup

# Load environment variables from .env if present
if os.path.exists(".env"):
    with open(".env", "r", encoding="utf-8") as f_env:
        for line in f_env:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip().strip('"').strip("'")

# Import google-genai
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

app = FastAPI(title="Movie Scraper UI")

# Force stdout to UTF-8 to prevent encoding crashes on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Mount posters directory to serve local images
if os.path.exists("posters"):
    app.mount("/posters", StaticFiles(directory="posters"), name="posters")

# Ensure static folder exists and mount it
os.makedirs("static", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = os.path.join("static", "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="index.html not found in static folder")
    with open(index_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/api/movies")
async def get_movies():
    html_file = "page1.html"
    if not os.path.exists(html_file):
        raise HTTPException(
            status_code=404, 
            detail="No scraped movie page (page1.html) found. Please run the scraper first."
        )
        
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        movie_cards = soup.select(".el-card.item")
        movies = []
        
        for idx, card in enumerate(movie_cards, 1):
            title_h2 = card.select_one("h2")
            title = title_h2.get_text(strip=True) if title_h2 else f"Movie_{idx}"
            
            title_cn = title
            title_en = ""
            if " - " in title:
                parts = title.split(" - ", 1)
                title_cn = parts[0].strip()
                title_en = parts[1].strip()
                
            cat_spans = card.select(".categories button span")
            categories = [span.get_text(strip=True) for span in cat_spans]
            
            info_divs = card.select(".info")
            regions = ""
            duration = ""
            release_date = ""
            if len(info_divs) > 0:
                info_text = info_divs[0].get_text(strip=True)
                if "/" in info_text:
                    parts = info_text.split("/", 1)
                    regions = parts[0].strip()
                    duration = parts[1].strip()
                else:
                    regions = info_text
            if len(info_divs) > 1:
                release_date = info_divs[1].get_text(strip=True).replace(" 上映", "").strip()
                
            score_p = card.select_one(".score")
            score = float(score_p.get_text(strip=True)) if score_p else 0.0
            
            detail_a = card.select_one("a[href*='/detail/']")
            detail_link = ""
            if detail_a:
                href = detail_a.get("href", "")
                detail_link = f"https://ssr1.scrape.center{href}" if href.startswith("/") else href
                
            # Serve local high-quality poster if available, otherwise fallback to remote URL
            poster_path = f"/posters/movie_{idx}.jpg"
            if not os.path.exists(f"posters/movie_{idx}.jpg"):
                cover_img = card.select_one("img.cover")
                poster_path = cover_img.get("src", "") if cover_img else ""
                if poster_path and "@" in poster_path:
                    poster_path = poster_path.split("@")[0]
                
            movies.append({
                "id": idx,
                "title_cn": title_cn,
                "title_en": title_en,
                "categories": categories,
                "regions": regions,
                "duration": duration,
                "release_date": release_date or "N/A",
                "score": score,
                "detail_link": detail_link,
                "poster_url": poster_path
            })
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse movie data: {str(e)}")

@app.get("/api/download")
async def download_excel():
    excel_file = "movies_with_posters.xlsx"
    if not os.path.exists(excel_file):
        raise HTTPException(
            status_code=404, 
            detail="Excel file movies_with_posters.xlsx not found. Please run the create_excel.py script first."
        )
    return FileResponse(
        excel_file, 
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
        filename="movies_with_posters.xlsx"
    )

@app.post("/api/chat")
async def chat_endpoint(payload: dict):
    user_msg = payload.get("message", "").strip()
    if not user_msg:
        return {"response": "Hi! I am your movie assistant. Ask me about the movies in this database (e.g. 'Recommend a movie', 'What is the top rated movie?', or search by category/year/country)."}
        
    try:
        # Load the movies data using our existing get_movies helper
        movies = await get_movies()
    except Exception as e:
        return {"response": f"Sorry, I had trouble reading the movie database: {str(e)}"}
        
    # Check if Gemini API key is configured
    api_key = os.environ.get("GEMINI_API_KEY")
    if GENAI_AVAILABLE and api_key:
        try:
            # Initialize client with key
            client = genai.Client(api_key=api_key)
            
            # Format the movie context for the LLM
            movies_json = json.dumps(movies, ensure_ascii=False, indent=2)
            
            system_instruction = f"""
You are a helpful, premium AI Movie Assistant. 
You are given a JSON database containing 100 top movies scraped from Scrape Center.
Your job is to answer user queries about these movies in a helpful, engaging way.

Database of Movies (JSON):
{movies_json}

INSTRUCTIONS FOR OUTPUT FORMATTING:
1. You MUST respond using HTML format for rich text formatting. The frontend renders your output as HTML using innerHTML.
2. Use <b>bold</b> tags to highlight movie titles and key points.
3. Use <br> tags for line breaks instead of newlines.
4. When suggesting or referencing a movie, always make it a clickable hyperlink to its detail page. 
   Use the exact detail_link from the database. Format the link like:
   <a href="DETAIL_LINK_HERE" target="_blank" style="color: #3b82f6; text-decoration: underline; font-weight: 600;">CHINESE_TITLE_HERE</a>
5. Use bulleted lists using standard text dashes (-) and <br> or HTML list tags.
6. Keep your answers concise, informative, and friendly.
7. If the user asks for movies not in the database, prioritize recommending movies from this database, but you can briefly mention external movies if relevant.
"""
            
            # Call Gemini 2.5 Flash
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_msg,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7
                )
            )
            
            if response.text:
                return {"response": response.text.replace("\n", "<br>")}
            else:
                return {"response": "Received an empty response from Gemini. Please try again."}
                
        except Exception as e:
            # Fall back to offline rules if API call fails
            print(f"Gemini API Error, falling back to offline rules: {e}")
            offline_resp = get_offline_response(user_msg, movies)
            return {
                "response": f"<span style='color: #ef4444; font-size: 0.8rem; display: block; margin-bottom: 0.5rem;'>[System: Gemini API call failed, fell back to offline rules. Error: {str(e)}]</span>" + offline_resp
            }
    else:
        # Fall back to offline rules if API key not found
        offline_resp = get_offline_response(user_msg, movies)
        return {
            "response": "<span style='color: #eab308; font-size: 0.8rem; display: block; margin-bottom: 0.5rem;'>⚠️ Offline Mode: To activate Gemini 2.5 Flash, please set GEMINI_API_KEY in your .env file.</span>" + offline_resp
        }

def get_offline_response(user_msg: str, movies: list) -> str:
    user_msg = user_msg.lower()
    
    # 1. Top rated movies query
    if any(k in user_msg for k in ["best", "top", "highest", "rating", "score", "最高", "评分"]):
        top_movies = sorted(movies, key=lambda x: x["score"], reverse=True)[:3]
        response_text = "Here are the top-rated movies in our list:<br>"
        for m in top_movies:
            response_text += f"- 🎬 **{m['title_cn']}** ({m['title_en']}) - Rating: ⭐ **{m['score']}**<br>"
        return response_text
        
    # 2. Recommendations query
    if any(k in user_msg for k in ["recommend", "suggest", "any good", "random", "推荐"]):
        import random
        m = random.choice(movies)
        return (f"I recommend watching **{m['title_cn']}** ({m['title_en']})!<br><br>"
                f"🎬 **Categories**: {', '.join(m['categories'])}<br>"
                f"🌍 **Region**: {m['regions']}<br>"
                f"⏱️ **Duration**: {m['duration']}<br>"
                f"⭐ **Score**: {m['score']}<br>"
                f"🔗 [Link to detail page]({m['detail_link']})")
        
    # 3. Check for specific categories
    categories_set = set()
    for m in movies:
        for c in m["categories"]:
            categories_set.add(c.lower())
            
    matched_category = None
    for cat in categories_set:
        if cat in user_msg:
            matched_category = cat
            break
            
    # English categories mapping
    en_to_cn_cat = {
        "drama": "剧情", "romance": "爱情", "action": "动作", "comedy": "喜剧",
        "crime": "犯罪", "thriller": "惊悚", "mystery": "悬疑", "fantasy": "奇幻",
        "adventure": "冒险", "animation": "动画", "sci-fi": "科幻", "war": "战争",
        "history": "历史", "biography": "传记", "family": "家庭"
    }
    for en, cn in en_to_cn_cat.items():
        if en in user_msg:
            matched_category = cn.lower()
            break
            
    if matched_category:
        cat_movies = [m for m in movies if any(c.lower() == matched_category for c in m["categories"])][:5]
        if cat_movies:
            response_text = f"Here are some popular **{matched_category.capitalize()}** movies:<br>"
            for m in cat_movies:
                response_text += f"- **{m['title_cn']}** - ⭐ **{m['score']}** ({m['regions']})<br>"
            return response_text

    # 4. Check for regions/countries
    regions_set = set()
    for m in movies:
        for r in m["regions"].split("、"):
            regions_set.add(r.strip().lower())
            
    matched_region = None
    for reg in regions_set:
        if reg in user_msg:
            matched_region = reg
            break
            
    # Common English-to-Chinese country mappings
    en_to_cn_reg = {
        "usa": "美国", "united states": "美国", "uk": "英国", "japan": "日本", 
        "france": "法国", "germany": "德国", "india": "印度", "hong kong": "中国香港",
        "china": "中国大陆", "italy": "意大利", "canada": "加拿大"
    }
    for en, cn in en_to_cn_reg.items():
        if en in user_msg:
            matched_region = cn.lower()
            break
            
    if matched_region:
        reg_movies = [m for m in movies if matched_region in m["regions"].lower()][:5]
        if reg_movies:
            response_text = f"Here are some top movies from **{matched_region.upper()}**:<br>"
            for m in reg_movies:
                response_text += f"- **{m['title_cn']}** - ⭐ **{m['score']}** ({m['duration']})<br>"
            return response_text
            
    # 5. Check if user mentioned a specific movie title
    matched_movie = None
    for m in movies:
        if m["title_cn"].lower() in user_msg or (m["title_en"] and m["title_en"].lower() in user_msg):
            matched_movie = m
            break
            
    if matched_movie:
        return (f"Here details for **{matched_movie['title_cn']}**:<br><br>"
                f"🎬 **Original Title**: {matched_movie['title_en']}<br>"
                f"🏷️ **Categories**: {', '.join(matched_movie['categories'])}<br>"
                f"🌍 **Region**: {matched_movie['regions']}<br>"
                f"⏱️ **Duration**: {matched_movie['duration']}<br>"
                f"⭐ **Score**: {matched_movie['score']}<br>"
                f"📅 **Release Date**: {matched_movie['release_date']}<br>"
                f"🔗 [Link to detail page]({matched_movie['detail_link']})")
        
    return ("I'm not sure I understood. I can help you with:<br>"
            "- Recommending a movie (type **recommend**)<br>"
            "- Finding the best movies (type **best** or **top rated**)<br>"
            "- Finding movies by genre (type **action**, **comedy**, **romance**, etc.)<br>"
            "- Searching by country (type **Japan**, **USA**, **France**, etc.)<br>"
            "- Inquiring about a specific movie title.")

# Mount static folder for CSS/JS assets (after defining specific endpoints)
app.mount("/", StaticFiles(directory="static"), name="static_root")
