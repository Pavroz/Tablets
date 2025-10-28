import pytest
import pytest
import os
import allure

@allure.feature('Авторизация')
class TestAuth:
    @allure.story('Негативные сценарий - невалидные данные')
    @allure.title('Проверка авторизации с некорректным логином')
    @pytest.mark.auth
    def test_incorrect_login(self, auth_page):
        auth_page.open()
        auth_page.auth_incorrect_login('qwe', '321')

    @allure.story('Негативные сценарий - невалидные данные')
    @allure.title('Проверка авторизации с некорректным паролем')
    @pytest.mark.auth
    def test_incorrect_password(self, auth_page):
        auth_page.open()
        auth_page.auth_incorrect_password('0', 'qwe')

    @allure.story('Сценарий восстановления конфигурации')
    @allure.title('Проверка авторизации с активным восстановлением конфигурации')
    @pytest.mark.auth
    def test_active_recovery_conf(self, auth_page):
        auth_page.open()
        auth_page.auth_active_recovery_conf('0', '321')

    @allure.story('Сценарий восстановления конфигурации')
    @allure.title('Проверка авторизации с неактивным восстановлением конфигурации')
    @pytest.mark.auth
    def test_inactive_recovery_conf(self, auth_page):
        auth_page.open()
        auth_page.auth_inactive_recovery_conf('0', '321')
