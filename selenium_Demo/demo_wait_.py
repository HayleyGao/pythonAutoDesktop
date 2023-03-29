from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import  unittest

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



# 强制等待
# time.sleep(2)


# 显式等待
# 较为智能的等待机制
# 若是在指定的等待的时间内找到元素，则提前终止轮询，而继续执行后续语句。
# 若是设定的等待时间内依然找不到元素，则抛出异常。
# WebDriverWait(driver, 10, 0.2)，10为指定的等待时间，0.2为调用频率，也就是多长的周期执行判断条件，默认为0.5。
driver.get("https://zhidao.baidu.com")
# loc=driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div/div/form/input")
ele=WebDriverWait(driver, 10, 0.2).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div["
                                                                                    "2]/header/div/div/div/form/input")))
if ele is not None:
    print(type(ele))
    ele.send_keys("python开发")

search_btn = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
search_btn.click()
driver.quit()



# 隐式等待
# 页面的全部元素都展现出来，才会执行后续语句。
# 若是全部页面元素展现的时间小于等待时间，则提前终止轮询，而继续执行后续语句。
# 若是设定的等待时间内依然找不到元素，则抛出异常。

# 和sleep()的区别就是，不会强制等待指定的时间。




