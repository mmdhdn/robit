from playwright.sync_api import sync_playwright

def run_miniapp(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)
        try:
            page.click("text=Enter Giveaway")
            print("کلیک روی Enter Giveaway انجام شد")
        except:
            print("دکمه یافت نشد")
        browser.close()
