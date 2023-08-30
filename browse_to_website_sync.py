from playwright.sync_api import sync_playwright


def open_youtube_with_chromium():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.youtube.com")

        browser.close()


if __name__ == "__main__":
    open_youtube_with_chromium()
