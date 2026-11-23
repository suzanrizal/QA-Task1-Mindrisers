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
        self.banana_add_to_cart_button_XPATH = (By.XPATH, "//div[2]//div[1]//div[2]//div[1]//button[1]")
        self.chicken_add_to_cart_button_XPATH = (By.XPATH, "//div[8]//div[1]//div[2]//div[1]//button[1]")
        self.potato_add_to_cart_button_XPATH = (By.XPATH, "//div[14]//div[1]//div[2]//div[1]//button[1]")
        self.strawberry_add_to_cart_button_XPATH = (By.XPATH, "//div[18]//div[1]//div[2]//div[1]//button[1]")

        #Alert
        self.alert_locator = (By.XPATH, "//div[@role='alert']")



    def click_shop_dropdown(self):
        self.driver.find_element(*self.dropdown_menu).click()

    def choose_meat_dropwown(self):
        self.driver.find_element(*self.meat_option).click()

    def choose_vegetables_option(self):
        self.driver.find_element(*self.vegetables_option).click()

    def add_banana_to_cart(self):
        self.driver.find_element(*self.banana_add_to_cart_button_XPATH).click()

    def add_chicken_to_cart(self):
        self.driver.find_element(*self.chicken_add_to_cart_button_XPATH).click()

    def add_potato_to_cart(self):
        self.driver.find_element(*self.potato_add_to_cart_button_XPATH).click()

    def add_strawberry_to_cart(self):
        self.driver.find_element(*self.strawberry_add_to_cart_button_XPATH).click()

    def get_alert_message(self):
        actual_message = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.alert_locator)
        )
        return actual_message.text

    # def scroll_to_chicken(self, driver):
    #     element = driver.find_element(
    #         *self.chicken_add_to_cart_button_XPATH
    #     )

    #     print("Element type:", type(element))

    #     driver.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'});",
    #         element
    #     )


        
