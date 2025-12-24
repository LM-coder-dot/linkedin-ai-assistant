from playwright.sync_api import sync_playwright
import os
import time

class LinkedInCollector:
    def __init__(self):
        self.cookie = os.getenv("LINKEDIN_COOKIE")
        if not self.cookie:
            raise RuntimeError("LINKEDIN_COOKIE not set")

    def collect(self, profile_url: str, limit: int = 20):
        posts = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()

            # LinkedIn Auth Cookie
            context.add_cookies([{
                "name": "li_at",
                "value": self.cookie,
                "domain": ".linkedin.com",
                "path": "/"
            }])

            page = context.new_page()
            page.goto(profile_url)
            page.wait_for_timeout(5000)

            post_elements = page.locator("div.feed-shared-update-v2")[:limit]

            for post in post_elements.all():
                text = post.inner_text()
                posts.append({
                    "text": text,
                    "post_url": profile_url,
                })

            browser.close()

        return posts
