import time
from playwright.sync_api import sync_playwright

if __name__ == "__main__":
    email = "vitici3157@wiemei.com"
    password = "roarlikeatigerwould1234!@#$"

    with sync_playwright() as p:
        # login
        print("Launching chrome")
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://accounts.spotify.com/en/login")
        print("Going to Spotify Login...")
        page.fill("input#login-username", email)
        time.sleep(2)
        page.fill("input#login-password", password)
        time.sleep(2)
        page.click("button#login-button")
        print("Waiting for login...")
        time.sleep(10)
        page.goto("https://spotify.com")
        time.sleep(100)
        page.close()
        browser.close()
