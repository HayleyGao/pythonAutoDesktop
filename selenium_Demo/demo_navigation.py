from selenium import webdriver
import time

driver = webdriver.Chrome()


# 浏览器的后退、前进、刷新操作

def isEqual(str1, str2):
    if str1 == str2:
        print("driver.current_url: ", driver.current_url)
    else:
        print('error，与预期字符串不相等')


base_url1 = "https://www.baidu.com/"
base_url2 = "https://fanyi.baidu.com/"

driver.get(base_url1)
time.sleep(1)
print("driver.current_url: ", driver.current_url)

driver.get(base_url2)
time.sleep(1)
print("driver.current_url: ", driver.current_url)

print("start back...")
driver.back()
time.sleep(2)

# print("driver.current_url: ", driver.current_url,'base_url1',base_url1)
isEqual(driver.current_url, base_url1)

print("start forward...")
driver.forward()
time.sleep(1)
isEqual(driver.current_url, base_url2)

time.sleep(1)

print("start refresh...")
driver.refresh()
time.sleep(1)
isEqual(driver.current_url, base_url2)
