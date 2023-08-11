import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables from .env file
load_dotenv()

# Constants
FORM_LINK = os.getenv("FORM_LINK")
GOOGLE_USERNAME = os.getenv("GOOGLE_USERNAME")
GOOGLE_PASSWORD = os.getenv("GOOGLE_PASSWORD")


class FormFiller:
    """A class to interact with and fill out a specific Google Form using Selenium."""

    def __init__(self):
        """Initializes the Selenium Chrome WebDriver."""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def fill_form(self, address, price, link):
        """
        Fills out the Google Form with the given address, price, and link.

        Parameters:
        - address (str): The address of the listing.
        - price (str): The price of the listing.
        - link (str): The URL link of the listing.
        """
        try:
            self.driver.get(FORM_LINK)
            # Input address
            address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
            address_input = self._wait_for_element_by_xpath(address_xpath)
            address_input.send_keys(address)

            # Input price
            price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
            price_input = self._wait_for_element_by_xpath(price_xpath)
            price_input.send_keys(price)

            # Input link
            link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
            link_input = self._wait_for_element_by_xpath(link_xpath)
            link_input.send_keys(link)

            # Submit the form
            self._submit_form()
        except Exception as e:
            print(f"Error while filling form: {e}")

    def _submit_form(self):
        """Private method to submit the Google Form."""
        try:
            submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
            submit_button = self.driver.find_element(By.XPATH, submit_button_xpath)
            submit_button.click()
        except UnexpectedAlertPresentException:
            alert = Alert(self.driver)
            alert.accept()

    def _wait_for_element_by_xpath(self, xpath, timeout=10):
        """
        Private method to wait for an element to be clickable using its XPath.

        Parameters:
        - xpath (str): The XPath of the desired element.
        - timeout (int, optional): The maximum time to wait for the element. Defaults to 10 seconds.

        Returns:
        - WebElement: The Selenium WebElement if found; None otherwise.
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
