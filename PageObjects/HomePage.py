from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

class HomePage:
    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

        # Implicit wait
        self.driver.implici
