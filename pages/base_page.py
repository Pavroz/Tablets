from typing import Tuple, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    base_url = 'http://arm-tablets.01-bfv-server.stroki.loc'
    page_url = None
    default_timeout = 10  # Устанавливаем таймаут по умолчанию

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            self.driver.get(self.base_url)

    # ФУНКЦИИ ДЛЯ ОЖИДАНИЙ
    def wait_for_clickable(self, locator, timeout: int = None) -> WebElement:
        """Ожидание, пока элемент станет кликабельным"""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        """Ожидание, пока элемент станет видимым"""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_all_visible(self, locator: Tuple[str, str], timeout: int = None) -> List[WebElement]:
        """Ожидание, пока список элементов станет видимым"""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def wait_for_presence(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        """Ожидание, пока элемент появится в DOM."""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))