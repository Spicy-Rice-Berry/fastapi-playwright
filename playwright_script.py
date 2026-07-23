
from pathlib import Path
from playwright.sync_api import sync_playwright

def search_strawberry():
    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.google.com")

        # Type strawberry
        page.locator("textarea[name='q']").fill("strawberry")

        # Press Enter
        page.keyboard.press("Enter")

        # Wait for search results
        page.wait_for_load_state("networkidle")

        # Save screenshot
        page.screenshot(path="output/strawberry_results.png")

        print("Screenshot saved to output/strawberry_results.png")

        browser.close()

if __name__ == "__main__":
    search_strawberry()

