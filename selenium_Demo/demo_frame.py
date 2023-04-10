from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 不同弹窗的处理办法
# alert、prompt、confirm

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_option)

chrome_driver.get("http://192.168.0.102/index.html")
chrome_driver.maximize_window()

time.sleep(2)

chrome_driver.switch_to.frame(1)  # 切换到body框架
chrome_driver.switch_to.frame(0)  # 切换到body的子框架0

a_=chrome_driver.find_element(By.XPATH, "/html/body/div/a[3]")
print(a_.text)  # 判断，成功找到定位的元素
a_.click()

