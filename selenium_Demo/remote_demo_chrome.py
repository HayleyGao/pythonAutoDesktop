import time
from selenium import webdriver

print("start ...")

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')
chrome_options.set_capability("browserVersion", "98")

driver = webdriver.Remote(
    command_executor='http://192.168.1.8:4444/wd/hub',
    options=chrome_options
)

driver.get("https://zhidao.baidu.com")

print("chrome:", driver.current_url)


driver.save_screenshot('current_url_by_chrome.png')
time.sleep(2)

driver.close()
