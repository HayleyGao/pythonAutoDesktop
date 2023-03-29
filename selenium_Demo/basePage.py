from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import json, time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://cn.bing.com"
        self.timeout = 15

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)

    def quit(self):
        self.driver.quit()
