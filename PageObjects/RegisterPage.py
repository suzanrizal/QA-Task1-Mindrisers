# Importing Essential modules, class
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver: webdriver.Chrome):  # initializing the driver
        self.driver = driver
        
        # Implicit Wait
        self.driver.implicitly_wait(10)

        # Saving Locators in a variable
        self.Signin_button = (By.XPATH, "//a[normalize-space()='Sign in']")
        self.create_new_Account_button= (By.XPATH, "//a[normalize-space()='Create an account']")
        self.email_textbox = (By.ID, "RegisterInput.Email")
        self.password_textbox = (By.ID, "RegisterInput.Password")
        self.confirm_password_textbox = (By.ID, "RegisterInput.ConfirmPassword")
        self.first_name_textbox = (By.ID, "RegisterInput.FirstName")
        self.last_name_textbox = (By.ID, "RegisterInput.LastName")
        self.register_button = (By.XPATH, "//button[@type='submit']")

        # Error meassge locators
        self.First_name_error = (By.CLASS_NAME, "text-danger")
        self.invalid_email_error = (By.CSS_SELECTOR,".text-danger")

    def click_signin(self):
        self.driver.find_element(*self.Signin_button).click()

    def click_create_new_account(self):
        self.driver.find_element(*self.create_new_Account_button).click() # * takes the values inside thetuple and pass them individually to the function.

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).clear()   # Clears the field first
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).clear()    # Clear password field first
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_textbox).clear()
        self.driver.find_element(*self.confirm_password_textbox).send_keys(confirm_password)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_textbox).clear()
        self.driver.find_element(*self.first_name_textbox).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_textbox).clear()
        self.driver.find_element(*self.last_name_textbox).send_keys(last_name)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def get_firstname_error_message(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.First_name_error))
        return error.text

    def get_invalid_email_error_message(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.invalid_email_error))
        return error.text


    

    



        
        
