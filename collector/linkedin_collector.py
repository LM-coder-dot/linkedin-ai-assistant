from playwright.sync_api import sync_playwright
import time
import os


class LinkedInCollector:
    def collect(self, limit: int = 10):
        posts = []

        if not os.path.exists("linkedin_state.json"):
            raise RuntimeError("linkedin_state.json fehlt – erst Login durchführen")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                storage_state="linkedin_state.json"
            )
            page = context.new_page()

            page.goto(
                "https://www.linkedin.com/feed/",
                wait_until="domcontentloaded",
                timeout=60000,
            )

            time.sleep(5)

            post_elements = page.locator("div.feed-shared-update-v2").all()

            for post in post_elements[:limit]:
                try:
                    text = post.inner_text(timeout=2000).strip()
                    if text:
                        posts.append({
                            "text": text,
                            "post_url": "https://www.linkedin.com/feed/",
                        })
                except Exception:
                    continue

            browser.close()

        return posts
