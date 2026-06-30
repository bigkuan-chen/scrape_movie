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
        "# Movie Scraping Project",
        "",
        "This project scrapes movie data from [Scrape Center (SSR1)](https://ssr1.scrape.center/page/1), downloads and resizes the movie posters, and exports them into various formats including Markdown, CSV, and Excel.",
        "",
        "## Project Structure",
        "- `scrape.py`: Scrapes the webpage and saves the raw HTML as `page1.html`.",
        "- `parse_movies.py`: Parses the HTML and saves the movie details into `movies.csv` and `movies.md`.",
        "- `create_excel.py`: Downloads posters, resizes them, and inserts them into an Excel workbook (`movies_with_posters.xlsx`).",
        "- `movies_with_posters.xlsx`: The final generated Excel spreadsheet with embedded poster images.",
        "- `README.md`: This file, showing all the movie cards details and poster thumbnails.",
        "",
        "## Scraped Movie List (Page 1)",
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
