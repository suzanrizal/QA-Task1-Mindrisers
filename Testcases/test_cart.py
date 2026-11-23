from selenium import webdriver
import pytest
from PageObjects.cartPage import CartPage
import time
from PageObjects.loginPage import LoginPage

class TestCartPage:
    @pytest.fixture(autouse=True)
    def setup(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://demo.ecommerce.endpointdev.com/auth/login")
        self.loginobj = LoginPage(self.driver)  # Loginpage object
        self.loginobj.enter_email("tester@yopmail.com")
        self.loginobj.enter_password("Sujan@123")
        self.loginobj.click_signin()
        self.cartobj = CartPage(self.driver) # CartPage Object

    def test_add_to_cart_functionality():
        self.


    