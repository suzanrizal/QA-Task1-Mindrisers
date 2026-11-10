from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

        # Implicit wait
        self.driver.implicitly_wait(10)
        #Locators
        self.dropdown_menu = (By.ID, "navbarDropdown")
        self.meat_option = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li.nav-item.dropdown > ul > li:nth-child(6) > a")
        self.vegetables_option = (By.CSS_SELECTOR, "li:nth-child(9) a:nth-child(1)")








    def click_shop_dropdown(self):
        self.driver.find_element(*self.dropdown_menu).click()

    def choose_meat_dropwown(self):
        self.driver.find_element(*self.meat_option).click()

    def choose_vegetables_option(self):
        self.driver.find_element(*self.vegetables_option).click()
        
