import pytest
import allure
from data import data_test

@allure.feature('Авторизация')
class TestAuth:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации')
    @pytest.mark.auth
    def test_correct_login(self, auth_page):
        auth_page.open()
        auth_page.auth_correct_login_and_password(data_test.login, data_test.password)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации с активным восстановлением конфигурации')
    @pytest.mark.auth
    def test_active_recovery_conf(self, auth_page):
        auth_page.open()
        auth_page.auth_active_recovery_conf(data_test.login, data_test.password)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации с неактивным восстановлением конфигурации')
    @pytest.mark.auth
    def test_inactive_recovery_conf(self, auth_page):
        auth_page.open()
        auth_page.auth_inactive_recovery_conf(data_test.login, data_test.password)

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустыми полями ввода')
    @pytest.mark.auth
    def test_empty_fields(self, auth_page):
        auth_page.open()
        auth_page.auth_empty_fields()

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином')
    @pytest.mark.auth
    def test_incorrect_login(self, auth_page):
        auth_page.open()
        auth_page.auth_incorrect_login('qwe', data_test.password)

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным паролем')
    @pytest.mark.auth
    def test_incorrect_password(self, auth_page):
        auth_page.open()
        auth_page.auth_incorrect_password(data_test.login, 'qwe')

