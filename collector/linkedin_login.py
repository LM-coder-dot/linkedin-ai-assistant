from playwright.sync_api import sync_playwright
import os

SESSION_PATH = "storage/linkedin_session.json"

def login_and_save_session():
    os.makedirs("storage", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=50
        )

        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.linkedin.com/login")

        print("➡️ Bitte jetzt MANUELL bei LinkedIn einloggen.")
        print("➡️ Sobald dein Feed sichtbar ist: ENTER drücken.")

        input()

        context.storage_state(path=SESSION_PATH)
        print(f"✅ Session gespeichert unter: {SESSION_PATH}")

        browser.close()

if __name__ == "__main__":
    login_and_save_session()
