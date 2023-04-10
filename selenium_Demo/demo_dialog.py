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
print(a_.text)
a_.click()

chrome_driver.switch_to.parent_frame()  # 从body子框架0切换到子框架1,需要先切换至父框架，再切回到子框架
chrome_driver.switch_to.frame(1)

# alert demo
chrome_driver.find_element(By.ID,"alert").click()
time.sleep(1)
alert_=chrome_driver.switch_to.alert
alert_.accept()
time.sleep(2)

# confirm demo
chrome_driver.find_element(By.ID,"confirm").click()
time.sleep(1)
confirm_=chrome_driver.switch_to.alert
# confirm_.accept()  # 确认按钮
confirm_.dismiss()  # 取消按钮
time.sleep(2)

# prompt demo
chrome_driver.find_element(By.ID,"prompt").click()
time.sleep(1)
prompt_=chrome_driver.switch_to.alert
prompt_.send_keys("孙小果")
# prompt_.accept()  # 确定按钮
prompt_.dismiss()  # 取消按钮

time.sleep(5)

chrome_driver.quit()









