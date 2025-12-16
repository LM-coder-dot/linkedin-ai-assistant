from playwright.sync_api import sync_playwright
import time

SESSION_PATH = "storage/linkedin_session.json"

def read_feed(max_scrolls=3):
    posts = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=80
        )

        context = browser.new_context(
            storage_state=SESSION_PATH,
            viewport={"width": 1280, "height": 800}
        )

        page = context.new_page()
        page.goto("https://www.linkedin.com/feed/")

        print("➡️ Feed geöffnet, warte auf Laden...")
        time.sleep(5)

        for i in range(max_scrolls):
            print(f"🔽 Scroll {i+1}/{max_scrolls}")

            # Post-Container
            post_elements = page.locator("div.feed-shared-update-v2")

            count = post_elements.count()
            print(f"   Gefundene Posts: {count}")

            for idx in range(count):
                try:
                    post = post_elements.nth(idx)

                    text = post.locator("span.break-words").inner_text(timeout=2000)
                    text = text.strip()

                    if text and text not in posts:
                        posts.append(text)

                except:
                    continue

            page.mouse.wheel(0, 1200)
            time.sleep(3)

        browser.close()

    return posts

if __name__ == "__main__":
    collected = read_feed()
    print("\n📌 GESAMMELTE POSTS:\n")
    for i, p in enumerate(collected, 1):
        print(f"{i}. {p[:120]}...\n")
