from selenium import webdriver
import pytest
from PageObjects.HomePage import HomePage
import time
from PageObjects.loginPage import LoginPage

class TestHomePage():
    @pytest.fixture(autouse=True)
    def setup(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://demo.ecommerce.endpointdev.com/auth/login")
        self.loginobj = LoginPage(self.driver)  # Loginpage object
        self.loginobj.enter_email("tester@yopmail.com")
        self.loginobj.enter_password("Sujan@123")
        self.loginobj.click_signin()
        self.homeobj = HomePage(self.driver)  # Homepage object


    def test_shop_dropdown_functionality(self, driver):
        self.homeobj.click_shop_dropdown()
        self.homeobj.choose_meat_dropwown()
        time.sleep(3)
        



