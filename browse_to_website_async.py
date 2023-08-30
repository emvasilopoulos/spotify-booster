import asyncio
from playwright.async_api import async_playwright


async def open_youtube_with_chromium(name: str):
    print("Running browser:", name)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.youtube.com")

        await asyncio.sleep(1)  # Simulate some activity
        await browser.close()


async def open_multiple_instances(num_instances):
    tasks = []
    base_name = "spotify_booster_browser_"
    for i in range(num_instances):
        name = f"{base_name}{i}"
        task = asyncio.create_task(open_youtube_with_chromium(name))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    num_instances = 3  # You can change this to the desired number of instances

    asyncio.run(open_multiple_instances(num_instances))
