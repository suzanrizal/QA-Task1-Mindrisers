from selenium import webdriver
import pytest
from PageObjects.loginPage import LoginPage
from readCSV import get_login_csv
import time

class TestLoginDDT():
    @pytest.fixture(autouse=True)
    def setup(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://demo.ecommerce.endpointdev.com/auth/login")
        
    @pytest.mark.parametrize("email, password, expected_result", get_login_csv())

    def test_login_DDT(self, email, password, expected_result):
        self.LoginObj = LoginPage(self.driver)
        self.LoginObj.enter_email(email)
        self.LoginObj.enter_password(password)
        self.LoginObj.click_signin()
        time.sleep(2)


        # Assertion
        if expected_result == "PASS":

            expected_url = "https://demo.ecommerce.endpointdev.com/"

            assert self.driver.current_url == expected_url, \
                f"Login failed! Actual URL: {self.driver.current_url}"

        elif expected_result == "FAIL":

            error_message = self.LoginObj.get_error_message()

            print(f"\nLogin Error: {error_message}")
