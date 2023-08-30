from playwright.sync_api import sync_playwright


def open_youtube_with_chromium():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.youtube.com")

        # You can add more interactions or actions here if needed

        input("Press Enter to close the browser...")

        browser.close()


if __name__ == "__main__":
    open_youtube_with_chromium()
