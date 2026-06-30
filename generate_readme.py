import os
import sys
import io
from bs4 import BeautifulSoup

# Force stdout to UTF-8 to prevent encoding crashes on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    html_file = "page1.html"
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found.")
        return
        
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    movie_cards = soup.select(".el-card.item")
    
    md_lines = [
        "# Movie Scraping Project & AI Assistant",
        "",
        "An elegant, fully-featured movie catalog web application that crawls pages, exports structured data, and embeds an interactive AI chat assistant.",
        "",
        "🚀 **Live Demo**: [https://scrape-movie.vercel.app/](https://scrape-movie.vercel.app/)",
        "",
        "## Key Features",
        "- 🕷️ **Crawl All Movies**: Overwrites the basic page 1 scraper to traverse all 10 pages of [Scrape Center (SSR1)](https://ssr1.scrape.center/) and fetch all 100 classic movies.",
        "- 🖼️ **High-Resolution Media**: Automatically strips CDN compression parameters to download high-resolution posters and downsamples crisp local thumbnails.",
        "- 📊 **Excel Integration**: Generates a custom-formatted `movies_with_posters.xlsx` spreadsheet containing the full metadata and compact poster thumbnails embedded directly in cell rows.",
        "- ⚡ **FastAPI Backend**: Serves API data routes, direct Excel download paths, and host routes in Python.",
        "- 🎨 **Premium UI**: Single Page Application styled with responsive vanilla CSS, featuring glassmorphism, fluid scaling, rating badges, search/filter panels, and light/dark theme toggles.",
        "- 🤖 **Gemini 2.5 Flash AI Assistant**: Interactive floating chat widget allowing natural language conversation about the movie database, with graceful offline rules fallback.",
        "- ☁️ **Vercel Serverless Ready**: Packaged configuration files for seamless Python ASGI deployment.",
        "",
        "## Project Structure",
        "- `scrape.py`: Crawls all pages and saves the combined HTML into `page1.html`.",
        "- `parse_movies.py`: Parses the HTML and generates `movies.csv` and `movies.md`.",
        "- `create_excel.py`: Downloads posters, generates thumbnails, and builds `movies_with_posters.xlsx`.",
        "- `main.py`: FastAPI server handling endpoints, static mounts, and Gemini API chatbot logic.",
        "- `vercel.json` & `requirements.txt`: Vercel serverless deployment specifications.",
        "- `README.md`: This file, detailing the project and showing the compiled movie database.",
        "",
        "## Getting Started Locally",
        "",
        "1. **Install Dependencies**:",
        "   ```bash",
        "   pip install -r requirements.txt",
        "   ```",
        "2. **Scrape & Parse Data**:",
        "   ```bash",
        "   python scrape.py",
        "   python create_excel.py",
        "   python parse_movies.py",
        "   ```",
        "3. **Configure API Key (Optional)**:",
        "   Create a `.env` file in the root folder and add your Gemini key:",
        "   ```env",
        "   GEMINI_API_KEY=your-api-key-here",
        "   ```",
        "4. **Launch Server**:",
        "   ```bash",
        "   python -m uvicorn main:app --reload",
        "   ```",
        "",
        "## Scraped Movie List (Page 1-10)",
        "",
        "| Poster | Chinese Title | English / Original Title | Categories | Regions / Countries | Duration | Release Date | Score |",
        "| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :---: |"
    ]
    
    for idx, card in enumerate(movie_cards, 1):
        # Title
        title_h2 = card.select_one("h2")
        title = title_h2.get_text(strip=True) if title_h2 else f"Movie_{idx}"
        
        # Split Title
        title_cn = title
        title_en = ""
        if " - " in title:
            parts = title.split(" - ", 1)
            title_cn = parts[0].strip()
            title_en = parts[1].strip()
            
        # Categories
        cat_spans = card.select(".categories button span")
        categories = ", ".join([span.get_text(strip=True) for span in cat_spans])
        
        # Info
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
            if not release_date:
                release_date = "N/A"
            
        # Score
        score_p = card.select_one(".score")
        score = score_p.get_text(strip=True) if score_p else "0.0"
        
        # Detail Link
        detail_a = card.select_one("a[href*='/detail/']")
        detail_link = ""
        if detail_a:
            href = detail_a.get("href", "")
            detail_link = f"https://ssr1.scrape.center{href}" if href.startswith("/") else href
            
        # Poster local path relative to project root
        poster_md_path = f"posters/resized/movie_{idx}.jpg"
        
        # Format poster tag (HTML format for sizing in markdown)
        poster_tag = f'<img src="{poster_md_path}" width="40" alt="{title_cn}">'
        
        # Title link
        title_link = f"[{title_cn}]({detail_link})" if detail_link else title_cn
        
        row = f"| {poster_tag} | {title_link} | {title_en} | {categories} | {regions} | {duration} | {release_date} | **{score}** |"
        md_lines.append(row)
        
    readme_content = "\n".join(md_lines) + "\n"
    
    with open("README.md", "w", encoding="utf-8") as f_out:
        f_out.write(readme_content)
        
    print("README.md successfully generated.")

if __name__ == "__main__":
    main()
