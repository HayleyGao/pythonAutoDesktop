from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import traceback

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)  # 设置保持chrome浏览器的打开状态
# https://www.selenium.dev/zh-cn/documentation/webdriver/browsers/chrome/

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://zhidao.baidu.com")
time.sleep(2)

try:
    input_ = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div/form/input-error")  # 这里故意设置错误地址
    input_.send_keys("python开发")
    search_btn = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
    search_btn.click()
    time.sleep(1)
except Exception as e:
    driver.save_screenshot("error.png")
    print(traceback.print_exc())  # 输出栈异常信息
finally:
    driver.quit()

