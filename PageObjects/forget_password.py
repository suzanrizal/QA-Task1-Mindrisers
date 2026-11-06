from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ForgetPasswordPage:
    def __init__(self, driver: webdriver.Chrome):  # initializing the driver
        self.driver = driver
        
        # Implicit Wait
        self.driver.implicitly_wait(10)

        # Saving Locators in a variable
        self.email_textbox = (By.XPATH, "//input[@id='ForgotPasswordInput.Email']")
        self.send_button = (By.XPATH, "//button[@type='submit']")

        # Error message locator
        self.email_error_message = (By.CSS_SELECTOR, ".text-danger")

        #Success message locator 
        self.sucess_message = (By.XPATH, "//div[@role='alert']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).clear()   # Clears field
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_submit(self):
        self.driver.find_element(*self.send_button).click()

    def get_email_field_error_message(self):
        email_error = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.email_error_message)
        )
        return email_error.text

    def get_sucess_messsage(self):
        success_message = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.sucess_message)
        )
        return success_message.text
        
         

   
        