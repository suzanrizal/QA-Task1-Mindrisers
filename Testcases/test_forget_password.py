from selenium import webdriver 
import time
import pytest
from PageObjects.forget_password import ForgetPasswordPage

class TestForgetPassword():
    @pytest.fixture(autouse=True)
    def setup(self, driver:webdriver.Chrome):  
        self.driver = driver
        driver.get("https://demo.ecommerce.endpointdev.com/auth/forgot-password")
        time.sleep(2)  # Wait for the page to load
        self.FPobj = ForgetPasswordPage(self.driver)

    def test_forget_password_with_valid_email(self, driver):
        self.FPobj.enter_email("testersujan@yopmail.com")
        self.FPobj.click_submit()
        time.sleep(2)  # Wait for the response
        self.FPobj.get_sucess_messsage()

        #Assertion
        actual_message = self.FPobj.get_sucess_messsage()
        expected_message = "A password reset link has been sent to your email."
        assert actual_message == expected_message
        print("Password reset success message verified!")

    def test_forget_password_with_invalid_email(self):
        self.FPobj.enter_email("email123")
        self.FPobj.click_submit()
        time.sleep(2)
        self.FPobj.get_email_field_error_message()

        #Assertion
        actual_message = self.FPobj.get_email_field_error_message()
        expected_message = "The Email field is not a valid e-mail address."
        assert actual_message == expected_message
        print("Reset link not sent for invalid email.")
        print(f"Error: {actual_message}")    # Prints what the actual error is 
        

       
        




