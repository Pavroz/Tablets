import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from pages.auth_page import AuthPage
from pages.profiles_page import ProfilesPage


@pytest.fixture()
def driver():
    """Создает и возвращает веб-драйвер с настройками"""
    options = Options()
    # Для ручного запуска
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--disable-cache")  # Отключает кэш
    ## Для CI
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver

@pytest.fixture()
def auth_page(driver):
    """Инициализация страницы авторизации"""
    return AuthPage(driver)

@pytest.fixture()
def profiles_page(driver):
    """Инициализация страницы профилей"""
    return ProfilesPage(driver)

@pytest.fixture()
def auth(auth_page):
    """Фикстура для авторизации"""
    auth_page.open()
    auth_page.auth_correct_login_and_password('0', '321')
