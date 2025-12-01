"""Scrape RevealJS documentation pages and save as HTML."""
import requests
import json
import time
from pathlib import Path

BASE_URL = "https://revealjs.com"
HTML_DIR = Path("html_pages")
PROGRESS_FILE = Path("scrape_progress.json")

PAGES = [
    "/",
    "/installation/",
    "/markup/",
    "/markdown/",
    "/backgrounds/",
    "/media/",
    "/lightbox/",
    "/code/",
    "/math/",
    "/fragments/",
    "/links/",
    "/layout/",
    "/slide-visibility/",
    "/themes/",
    "/transitions/",
    "/config/",
    "/presentation-size/",
    "/vertical-slides/",
    "/auto-animate/",
    "/auto-slide/",
    "/speaker-view/",
    "/scroll-view/",
    "/slide-numbers/",
    "/jump-to-slide/",
    "/touch-navigation/",
    "/pdf-export/",
    "/overview/",
    "/fullscreen/",
    "/initialization/",
    "/api/",
    "/events/",
    "/keyboard/",
    "/presentation-state/",
    "/postmessage/",
    "/plugins/",
    "/creating-plugins/",
    "/multiplex/",
    "/react/",
    "/upgrading/",
]

def load_progress():
    """Load progress from JSON file."""
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"completed": [], "failed": []}

def save_progress(progress):
    """Save progress to JSON file."""
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))

def get_filename(path):
    """Convert URL path to filename."""
    if path == "/":
        return "home.html"
    return path.strip("/").replace("/", "_") + ".html"

def scrape_page(path):
    """Scrape a single page and return its HTML content."""
    url = BASE_URL + path
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.text

def main():
    HTML_DIR.mkdir(exist_ok=True)
    progress = load_progress()

    for path in PAGES:
        if path in progress["completed"]:
            print(f"Skipping (already done): {path}")
            continue

        filename = get_filename(path)
        filepath = HTML_DIR / filename

        try:
            print(f"Scraping: {path}")
            html = scrape_page(path)
            filepath.write_text(html)
            progress["completed"].append(path)
            save_progress(progress)
            print(f"  -> Saved to {filepath}")
            time.sleep(0.5)  # Be polite to the server
        except Exception as e:
            print(f"  -> Failed: {e}")
            if path not in progress["failed"]:
                progress["failed"].append(path)
            save_progress(progress)

    print(f"\nDone! Completed: {len(progress['completed'])}, Failed: {len(progress['failed'])}")

if __name__ == "__main__":
    main()
