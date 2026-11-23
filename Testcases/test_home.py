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
        self.loginobj.enter_password("Tester@123")
        self.loginobj.click_signin()
        time.sleep(3)
        self.homeobj = HomePage(self.driver)  # Homepage object

    def test_shop_dropdown_meat_functionality(self):
        time.sleep(5)
        self.homeobj.click_shop_dropdown()
        time.sleep(2)
        self.homeobj.choose_meat_dropwown()
        time.sleep(2)
        print("Passed")

        #Assertion
        assert "4" in self.driver.current_url, "Test Failed"
        print("Test executed sucessfully")

    def test_shop_dropdown_vegetables_functionality(self):
        time.sleep(5)
        self.homeobj.click_shop_dropdown()
        time.sleep(2)
        self.homeobj.choose_vegetables_option()
        time.sleep(2)

        assert "2" in self.driver.current_url, "Test Failed"

    def test_add_to_cart_functionality(self, driver):
        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(2)
        self.homeobj.add_banana_to_cart()
        time.sleep(5)
        # driver.execute_script("window.scrollBy(0, 600);")
        self.homeobj.add_chicken_to_cart()
        time.sleep(2)
        # self.homeobj.add_potato_to_cart()
        # time.sleep(2)
        # self.homeobj.add_strawberry_to_cart()
        # time.sleep(2)

        actual_messsage = self.homeobj.get_alert_message()
        expected_message = "Item added to cart."
        assert actual_messsage == expected_message
        print("Products added to cart sucessfully") 
        
        



