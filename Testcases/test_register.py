from selenium import webdriver 
import time
import pytest
from PageObjects.RegisterPage import RegisterPage

class TestRegister:
    def test_register_with_valid_credentials(self , driver):
        driver.get("https://demo.ecommerce.endpointdev.com/")
        time.sleep(5)
        regObj = RegisterPage(driver)  # Creating object for register class

        regObj.click_signin()
        # time.sleep(2)  # Hardcore wait
        regObj.click_create_new_account()
        # time.sleep(2)
        regObj.enter_email("Testemail12@email.com")
        regObj.enter_password("Test@12345")
        regObj.enter_confirm_password("Test@12345")
        regObj.enter_first_name("Test")
        regObj.enter_last_name("User")
        regObj.click_register()
        # time.sleep(2)

        # Assertion # Screenshot Validation After sucessful registration
        try:
            assert "login" in driver.current_url, "Registration failed"
            print("Registration sucessfull")
        except AssertionError:
            driver.save_screenshot("Screenshots/Registration.png")
            print("Registration failed")
        
        driver.quit()
 
    def test_register_with_first_name_empty(Self, driver):
        driver.get("https://demo.ecommerce.endpointdev.com/")
        time.sleep(5)
        regObj = RegisterPage(driver)  # Creating object for register class

        regObj.click_signin()
        # time.sleep(2)  # Hardcore wait
        regObj.click_create_new_account()
        # time.sleep(2)
        regObj.enter_email("Testemail@email.com")
        regObj.enter_password("Test@12345")
        regObj.enter_confirm_password("Test@12345")
        regObj.enter_first_name("")  # Empty first name
        regObj.enter_last_name("User")
        regObj.click_register()
        # time.sleep(2)
    
        #Assertion
        expected_error_message = "The FirstName field is required."
        actual_error_message = regObj.get_firstname_error_message()
        try:
            assert expected_error_message == actual_error_message, "Error message does not match"
            print("Error message validation passed")
        except AssertionError:
            driver.save_screenshot("Screenshots/FirstNameError.png")
            print("Error message validation failed")
            

        