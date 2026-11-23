from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    
        # Implicit wait
        self.driver.implicitly_wait(10)

        #Locators
        self.cart_button_XPATH = (By.XPATH, "//a[@href='/cart']") 
        self.banana_quantity_XPATH = (By.XPATH, "//div[@class='container px-4 px-lg-5 my-5']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
        self.banana_update_button_XPATH = (By.XPATH, "//div[@class='container px-4 px-lg-5 my-5']//div[1]//div[1]//div[2]//div[1]//div[1]//button[1]")
        self.proceed_to_checkout_button = (By.XPATH, "//a[normalize-space()='Proceed to Checkout']")

