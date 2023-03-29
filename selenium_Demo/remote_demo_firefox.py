import time
from selenium import webdriver

print("start ...")

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor='http://192.168.1.8:4444/wd/hub',
    options=firefox_options
)

driver.get("https://zhidao.baidu.com")

print("firefox:", driver.current_url)
assert driver.current_url, 'https://zhidao.baidu.com'

driver.save_screenshot('current_url.png')
time.sleep(2)

driver.close()


