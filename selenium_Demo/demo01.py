from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import json, time


def run():
    print('start...')
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)  # 设置保持chrome浏览器的打开状态,不会运行完成之后自动关闭（需要设置close）
    # https://www.selenium.dev/zh-cn/documentation/webdriver/browsers/chrome/

    driver = webdriver.Chrome(options=chrome_option)

    driver.get("https://zhidao.baidu.com")

    time.sleep(2)
    driver.save_screenshot('current_url.png')

    input_ = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div/form/input")

    input_.send_keys("python开发")

    search_btn = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
    search_btn.click()

    # time.sleep(5)
    driver.quit()
    print('already quit!')


if __name__ == "__main__":
    run()
