import os
import sys
import io
import requests
import urllib3
from bs4 import BeautifulSoup

# Force stdout to UTF-8 to prevent encoding crashes on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Suppress urllib3 SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    base_url = "https://ssr1.scrape.center/page/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    combined_soup = None
    container = None
    
    print("Scraping all pages (1 to 10) of Scrape Center...")
    
    for page in range(1, 11):
        url = f"{base_url}{page}"
        print(f"Fetching page {page} from {url}...")
        try:
            response = requests.get(url, headers=headers, verify=False, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            if page == 1:
                combined_soup = soup
                # Find the container column holding the movie cards
                container = combined_soup.select_one("#index .el-col")
                if not container:
                    print("Error: Could not find movie cards container on page 1.")
                    return
            else:
                # Extract cards from subsequent pages and append to container in page 1 structure
                cards = soup.select("#index .el-card.item")
                for card in cards:
                    if container:
                        container.append(card)
                        
        except requests.exceptions.RequestException as e:
            print(f"Error scraping page {page}: {e}")
            
    if combined_soup:
        output_file = "page1.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(combined_soup))
        print(f"\nSuccessfully scraped all movies and saved to {output_file}")
    else:
        print("Error: No data scraped.")

if __name__ == "__main__":
    main()
