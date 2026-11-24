from selenium import webdriver
import pytest
from PageObjects.HomePage import HomePage
import time
from PageObjects.loginPage import LoginPage
from PageObjects.add_new_address import AddNewAddress

class TestHomePage():
    @pytest.fixture(autouse=True)
    def setup(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://demo.ecommerce.endpointdev.com/auth/login")
        self.loginobj = LoginPage(self.driver)  # Loginpage object
        self.loginobj.enter_email("tester@yopmail.com")
        self.loginobj.enter_password("Tester@1234")
        self.loginobj.click_signin()
        time.sleep(3)
        self.ANAobj = AddNewAddress(self.driver)

    def test_add_new_address(self, driver):
        self.ANAobj.clickMyAccount()
        self.ANAobj.clickAddresses()
        self.ANAobj.clickAddNewAddress()
        self.ANAobj.SetFirstName("Sujan")
        self.ANAobj.SetLastName("Rijal")
        self.ANAobj.SetStreetLine1("Kalanki")
        self.ANAobj.SetStreetLine2("Syuchatar")
        self.ANAobj.SetCity("Kathmandu")
        self.ANAobj.SelectState()
        self.ANAobj.SetZipCode(44600)
        self.ANAobj.SetPhoneNumber("9840308349")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, 500);")  # Scroll
        time.sleep(3)
        self.ANAobj.click_add_address_button()
        
        expected_messasge = "Address created successfully."
        actual_message = self.ANAobj.get_alert_message()
        assert expected_messasge == actual_message 
        print("Validation Sucessfull")