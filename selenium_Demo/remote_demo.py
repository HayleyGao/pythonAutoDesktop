import time
from selenium import webdriver


class TestZhiDao:
    chrome_options = webdriver.ChromeOptions()



    driver = webdriver.Remote(
        command_executor='http://192.168.1.8:4444/wd/hub',
        options=chrome_options
    )

    driver.get("https://zhidao.baidu.com")

    print("chrome:", driver.current_url)
    assert driver.current_url, 'https://zhidao.baidu.com'

    time.sleep(2)

    driver.quit()


if __name__ == "__name__":
    TestZhiDao()
