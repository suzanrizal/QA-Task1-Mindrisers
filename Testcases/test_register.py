from selenium import webdriver 
import time
import pytest
from PageObjects.RegisterPage import RegisterPage

class TestRegister:

    # Reusable setup for registration tests
    @pytest.fixture(autouse=True)  #This fixture runs for every test 
    def setup(self, driver):
        self.driver = driver
        self.regObj = RegisterPage(self.driver)

        self.driver.get("https://demo.ecommerce.endpointdev.com/")

        self.regObj.click_signin()
        self.regObj.click_create_new_account()

    def test_register_with_valid_credentials(self , driver):
        # driver.get("https://demo.ecommerce.endpointdev.com/")
        # time.sleep(5)  # Creating object for register class

        self.regObj.click_signin()
        # time.sleep(2)  # Hardcore wait
        self.regObj.click_create_new_account()
        # time.sleep(2)
        self.regObj.enter_email("Testemail12@email.com")
        self.regObj.enter_password("Test@12345")
        self.regObj.enter_confirm_password("Test@12345")
        self.regObj.enter_first_name("Test")
        self.regObj.enter_last_name("User")
        self.regObj.click_register()
        # time.sleep(2)

        # Assertion # Screenshot Validation After sucessful registration
        try:
            assert "login" in driver.current_url, "Registration failed"
            print("Registration sucessfull")
        except AssertionError:
            driver.save_screenshot("Screenshots/Registration.png")
            print("Registration failed")
 
    def test_register_with_first_name_empty(self, driver):  

        self.regObj.click_signin()
        # time.sleep(2)  # Hardcore wait
        self.regObj.click_create_new_account()
        # time.sleep(2)
        self.regObj.enter_email("Testemail@email.com")
        self.regObj.enter_password("Test@12345")
        self.regObj.enter_confirm_password("Test@12345")
        self.regObj.enter_first_name("")  # Empty first name
        self.regObj.enter_last_name("User")
        self.regObj.click_register()
        # time.sleep(2)
    
        #Assertion
        expected_error_message = "The FirstName field is required."
        actual_error_message = self.regObj.get_firstname_error_message()
        try:
            assert expected_error_message == actual_error_message, "Registration Passed with empty first name"
            print("Registration failed as expected with empty first name")
        except AssertionError:
            driver.save_screenshot("Screenshots/FirstNameError.png")
            print("Registration passed with empty first name")

    def test_register_with_invalid_email(self, driver):

        self.regObj.click_signin()
        self.regObj.click_create_new_account()
        self.regObj.enter_email("invalidemail.com")  # Invalid email format
        self.regObj.enter_password("Test@12345")
        self.regObj.enter_confirm_password("Test@12345")
        self.regObj.enter_first_name("Test")
        self.regObj.enter_last_name("User")
        self.regObj.click_register()

        # Assertion
        expected_error_message = "The Email field is not a valid e-mail address."
        actual_error_message = self.regObj.get_invalid_email_error_message()
        assert expected_error_message == actual_error_message, "Registration failed"
        

    def test_register_with_special_characters_in_first_name(self, driver):

        self.regObj.click_signin()
        self.regObj.click_create_new_account()
        self.regObj.enter_email("testemail@email.com")
        self.regObj.enter_password("Test@12345")
        self.regObj.enter_confirm_password("Test@12345")
        self.regObj.enter_first_name("@#$%^&*()")  # Special characters in first name
        self.regObj.enter_last_name("User")
        self.regObj.click_register()

        #Assertion without Try except
        assert "login" in driver.current_url, "Registration failed with special characters in first name"


    


    
            

        