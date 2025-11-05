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

    def go_to_back(self):
        self.got_to_back()

    def create_participant(self):
        # random = self.generate_random()
        self.wait_for_clickable(loc.create_button).click()
        sleep(2)
        lastname = self.wait_for_visible(loc.lastname_field)
        sleep(2)
        firstname = self.wait_for_visible(loc.firstname_field)
        sleep(2)
        lastname.send_keys(self.generate_random())
        sleep(2)
        firstname.send_keys(self.generate_random())
        sleep(2)
        self.wait_for_clickable(loc.create_button_in_modal).click()
        sleep(2)
        new_lastname = self.wait_for_presence((By.XPATH, f'//*[text()="{lastname}"]'))
        return new_lastname.text

    def update_participant(self, name):
        # name_p = name.text
        line_to_participant = self.wait_for_presence((By.XPATH, f'//*[text()="{name}"]'))
        sleep(2)
        line_to_participant.click()
        sleep(2)
        self.wait_for_clickable(loc.edit_button).click()
        sleep(2)
        lastname = self.wait_for_visible(loc.lastname_field)
        sleep(2)
        firstname = self.wait_for_visible(loc.firstname_field)
        sleep(2)
        lastname.send_keys(self.generate_random())
        sleep(2)
        firstname.send_keys(self.generate_random())
        sleep(2)
        self.wait_for_clickable(loc.save_button_in_modal).click()
        sleep(2)


