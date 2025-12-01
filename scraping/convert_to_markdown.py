"""Convert RevealJS HTML docs to clean Markdown."""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md

HTML_DIR = Path("html_pages")
MD_DIR = Path("markdown_pages")
PROGRESS_FILE = Path("convert_progress.json")

def load_progress():
    """Load progress from JSON file."""
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"completed": [], "failed": []}

def save_progress(progress):
    """Save progress to JSON file."""
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))

def extract_main_content(html):
    """Extract just the main article content from the HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Find the main article element
    article = soup.find("article", class_="article")
    if not article:
        return None

    # Remove the footer if present inside article
    footer = article.find("footer")
    if footer:
        footer.decompose()

    return article

def remove_demo_elements(soup):
    """Remove reveal demo/example elements that aren't useful in markdown."""
    # Remove reveal-example divs (interactive demos)
    for div in soup.find_all("div", class_="reveal-example"):
        div.decompose()
    for div in soup.find_all("div", class_="reveal"):
        div.decompose()
    return soup

def convert_html_to_markdown(html_content):
    """Convert HTML content to clean Markdown."""
    article = extract_main_content(html_content)
    if not article:
        return None

    # Remove demo elements
    article = remove_demo_elements(article)

    # Convert to markdown
    markdown = md(str(article), heading_style="ATX")

    # Clean up the markdown
    # Remove excessive blank lines
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    # Remove trailing whitespace
    markdown = '\n'.join(line.rstrip() for line in markdown.split('\n'))

    return markdown.strip()

def main():
    MD_DIR.mkdir(exist_ok=True)
    progress = load_progress()

    html_files = list(HTML_DIR.glob("*.html"))

    for html_file in html_files:
        if html_file.name in progress["completed"]:
            print(f"Skipping (already done): {html_file.name}")
            continue

        md_filename = html_file.stem + ".md"
        md_filepath = MD_DIR / md_filename

        try:
            print(f"Converting: {html_file.name}")
            html_content = html_file.read_text()
            markdown = convert_html_to_markdown(html_content)

            if markdown:
                md_filepath.write_text(markdown)
                progress["completed"].append(html_file.name)
                save_progress(progress)
                print(f"  -> Saved to {md_filepath}")
            else:
                print(f"  -> Could not extract content")
                progress["failed"].append(html_file.name)
                save_progress(progress)

        except Exception as e:
            print(f"  -> Failed: {e}")
            import traceback
            traceback.print_exc()
            if html_file.name not in progress["failed"]:
                progress["failed"].append(html_file.name)
            save_progress(progress)

    print(f"\nDone! Completed: {len(progress['completed'])}, Failed: {len(progress['failed'])}")

if __name__ == "__main__":
    main()
