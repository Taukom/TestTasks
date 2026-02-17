from selenium import webdriver

expected_title = "Fast and reliable end-to-end testing for modern web apps | Playwright"
link = "https://playwright.dev/"

browsers = {
    "Chrome": webdriver.Chrome,
    "Firefox": webdriver.Firefox
}

for name, BrowserClass in browsers.items():
    browser = BrowserClass()
    try:
        browser.get(link)
        title = browser.title
        if title == expected_title:
            print(f"{name}: Тест пройден")
        else:
            print(f"{name}: Тест провален (заголовок: {title})")
    finally:
        browser.quit()