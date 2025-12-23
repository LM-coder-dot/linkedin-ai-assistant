import os

cookie = os.getenv("LINKEDIN_COOKIE")
if not cookie:
    raise RuntimeError("LINKEDIN_COOKIE not set")

class LinkedInCollector:
    def collect_feed(self, limit=20):
        return [
            {
                "text": "FinTech und AI verändern die Banking-Welt massiv.",
                "author": "Anna Müller – FinTech Strategy",
                "post_url": "https://www.linkedin.com/posts/example1",
            },
            {
                "text": "Die neuesten Trends in Digital Market und Kryptowährungen.",
                "author": "Max Becker | Digital Banking",
                "post_url": "https://www.linkedin.com/posts/example2",
            },
            {
                "text": "Ein unauffälliger Beitrag ohne Relevanz.",
                "author": "Random User",
                "post_url": "https://www.linkedin.com/posts/example3",
            }
        ]
