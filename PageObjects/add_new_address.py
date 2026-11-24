from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddNewAddress:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    
        # Implicit wait
        self.driver.implicitly_wait(10)

        #Locators
        self.Myaccount_ID = (By.ID, "myAccountDropdown")
        self.Address_XPATH = (By.XPATH, "//a[normalize-space()='Addresses']")
        self.add_new_address_XPATH = (By.XPATH, "//a[normalize-space()='Add a new address']")
        self._first_name_ID = (By.ID, "Address_Name")
        self._last_name_ID = (By.ID, "Address_LastName")
        self._street_Line1_ID = (By.ID, "Address_Street")
        self._street_Line2_ID = (By.ID, "Address_StreetTwo")
        self.city_ID = (By.ID, "Address_City")
        self.state_dropdown_XPATH = (By.XPATH, "//select[@class='form-control valid']")
        self.Zip_code_ID =(By.ID, "Address_ZipCode")
        self.phoneno_ID = (By.ID, "Address_PhoneNumber")
        self.Add_address_button_XPATH = (By.XPATH, "//button[@type='submit']")

        # Alert locator
        self.alert_message_XPATH = (By.XPATH, "//div[@role='alert']")

    def clickMyAccount(self):
        self.driver.find_element(*self.Myaccount_ID).click()

    def clickAddresses(self):
        self.driver.find_element(*self.Address_XPATH).click()

    def clickAddNewAddress(self):
        self.driver.find_element(*self.add_new_address_XPATH).click()

    def SetFirstName(self, Fname):
        self.driver.find_element(*self._first_name_ID).send_keys(Fname)

    def SetLastName(self, Lname):
        self.driver.find_element(*self._last_name_ID).send_keys(Lname)

    def SetStreetLine1(self, Line1):
        self.driver.find_element(*self._street_Line1_ID).send_keys(Line1)

    def SetStreetLine2(self, Line2):
        self.driver.find_element(*self._street_Line2_ID).send_keys(Line2)

    def SetCity(self, City):
        self.driver.find_element(*self.city_ID).send_keys(City)

    def SelectState(self):
        Dropdown = Select(self.driver.find_element(*self.state_dropdown_XPATH))
        Dropdown.select_by_value("35")

    def SetZipCode(self, zip):
        self.driver.find_element(*self.Zip_code_ID).send_keys(zip)

    def SetPhoneNumber(self, PnNumber):
        self.driver.find_element(*self.phoneno_ID).send_keys(PnNumber)

    def click_add_address_button(self):
        self.driver.find_element(*self.Add_address_button_XPATH).click()

    def get_alert_message(self):
        actual_message = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.alert_message_XPATH)
        )
        return actual_message.text

    





