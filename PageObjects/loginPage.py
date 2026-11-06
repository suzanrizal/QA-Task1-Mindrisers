from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: webdriver.Chrome):  # initializing the driver
        self.driver = driver
        
        # Implicit Wait
        self.driver.implicitly_wait(10)

        # Saving Locators in a variable
        self.email_textbox = (By.ID, "LoginInput.Email")
        self.password_textbox = (By.ID, "LoginInput.Password")
        self.signin_button = (By.XPATH, "//button[@type='submit']")

        # Error message locator
        self.error_message = (By.CSS_SELECTOR, ".validation-message")

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).clear()   # Clears field
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).clear()    # Clears field
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_signin(self):
        self.driver.find_element(*self.signin_button).click()

    # def get_error_message(self):
    #     return self.driver.find_element(
    #         *self.error_message
    #     ).text

    # def get_email_error_message(self):
    #     error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message))
    #     return error.text

    # def get_password_error_message(self):
    #     error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message))
    #     return error.text

   