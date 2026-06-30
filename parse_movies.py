from bs4 import BeautifulSoup
import csv
import os
import sys
import io

# Force stdout to output UTF-8 to prevent console encoding issues on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def parse_html():
    file_path = "page1.html"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    movie_cards = soup.select(".el-card.item")
    
    movies_data = []
    
    for card in movie_cards:
        # 1. Detail link
        detail_a = card.select_one("a[href*='/detail/']")
        detail_link = ""
        if detail_a:
            href = detail_a.get("href", "")
            detail_link = f"https://ssr1.scrape.center{href}" if href.startswith("/") else href
            
        # 2. Cover image
        cover_img = card.select_one("img.cover")
        cover_url = cover_img.get("src", "") if cover_img else ""
        if cover_url and "@" in cover_url:
            cover_url = cover_url.split("@")[0]
        
        # 3. Title
        title_h2 = card.select_one("h2")
        title = title_h2.get_text(strip=True) if title_h2 else ""
        
        # Split title into Chinese and English/Original title
        title_cn = ""
        title_en = ""
        if " - " in title:
            parts = title.split(" - ", 1)
            title_cn = parts[0].strip()
            title_en = parts[1].strip()
        else:
            title_cn = title
            title_en = title
            
        # 4. Categories
        category_spans = card.select(".categories button span")
        categories = [span.get_text(strip=True) for span in category_spans]
        categories_str = ", ".join(categories)
        
        # 5. Info divs (Region, Duration, Release Date)
        info_divs = card.select(".info")
        
        regions = ""
        duration = ""
        release_date = ""
        
        # Usually the first info div contains region and duration separated by "/"
        if len(info_divs) > 0:
            first_info_text = info_divs[0].get_text(strip=True)
            if "/" in first_info_text:
                parts = first_info_text.split("/", 1)
                regions = parts[0].strip()
                duration = parts[1].strip()
            else:
                regions = first_info_text
                
        # The second info div contains release date
        if len(info_divs) > 1:
            release_text = info_divs[1].get_text(strip=True)
            release_date = release_text.replace(" 上映", "").strip()
            
        # 6. Score
        score_p = card.select_one(".score")
        score = score_p.get_text(strip=True) if score_p else ""
        
        movies_data.append({
            "Title (Chinese)": title_cn,
            "Title (English)": title_en,
            "Categories": categories_str,
            "Regions/Countries": regions,
            "Duration": duration,
            "Release Date": release_date,
            "Score": score,
            "Detail Link": detail_link,
            "Cover Image URL": cover_url
        })
        
    return movies_data

def write_csv(movies_data):
    csv_file = "movies.csv"
    fields = [
        "Title (Chinese)", "Title (English)", "Categories", 
        "Regions/Countries", "Duration", "Release Date", 
        "Score", "Detail Link", "Cover Image URL"
    ]
    
    with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(movies_data)
    print(f"Saved to {csv_file}")

def generate_markdown_table(movies_data):
    headers = [
        "Chinese Title", "English/Original Title", "Categories", 
        "Regions/Countries", "Duration", "Release Date", "Score"
    ]
    
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    
    for m in movies_data:
        title_link = f"[{m['Title (Chinese)']}]({m['Detail Link']})" if m['Detail Link'] else m['Title (Chinese)']
        row = [
            title_link,
            m["Title (English)"],
            m["Categories"],
            m["Regions/Countries"],
            m["Duration"],
            m["Release Date"],
            f"**{m['Score']}**"
        ]
        lines.append("| " + " | ".join(row) + " |")
        
    md_content = "\n".join(lines)
    with open("movies.md", "w", encoding="utf-8") as f:
        f.write("# Scraped Movies Information\n\n" + md_content)
    print("Saved to movies.md")
    return md_content

def main():
    movies_data = parse_html()
    if movies_data:
        write_csv(movies_data)
        md_table = generate_markdown_table(movies_data)
        print("\nParsed Movies Table:\n")
        print(md_table)

if __name__ == "__main__":
    main()
