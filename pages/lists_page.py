from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import lists_locators as loc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import allure
import random
import string

class ListsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def generate_random(prefix='Test_', length = 20):
        suffix = ''.join(random.choice(string.ascii_lowercase)
                         for _ in range(length))
        return f'{prefix}{suffix}'

    def create_participant(self):
        # random = self.generate_random()
        self.wait_for_clickable(loc.create_button).click()
        lastname = self.wait_for_visible(loc.lastname_field)
        firstname = self.wait_for_visible(loc.firstname_field)
        lastname.send_keys(self.generate_random())
        sleep(1)
        firstname.send_keys(self.generate_random())
        sleep(2)
        self.wait_for_clickable(loc.create_button_in_modal).click()
        sleep(5)
        self.got_to_back()
        sleep(2)


