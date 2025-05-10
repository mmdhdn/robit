from playwright.sync_api import sync_playwright

def run_miniapp(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        try:
            page.click("text=Enter Giveaway")
            print("🎯 کلیک روی Enter Giveaway انجام شد ✅")
        except Exception as e:
            print(f"❌ خطا در کلیک روی Enter Giveaway: {e}")
        browser.close()
