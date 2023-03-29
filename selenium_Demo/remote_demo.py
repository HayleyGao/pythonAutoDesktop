from selenium import webdriver
import  time


firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor='http://192.168.1.8:4444/grid/console',
    options=firefox_options
)
driver.get("http://www.baidu.com")
time.sleep(3)
driver.quit()
