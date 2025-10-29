from pages.base_page import BasePage
from pages.locators import auth_locators as loc
import allure

class AuthPage(BasePage):
    page_url = '/auth'

    def __init__(self, driver):
        super().__init__(driver)

    def auth_incorrect_login(self, login, password):
        with allure.step(f'Ввод логина "{login}"'):
            self.wait_for_visible(loc.login).send_keys(login)
        with allure.step(f'Ввод пароля "{password}"'):
            self.wait_for_visible(loc.password).send_keys(password)
        with allure.step('Нажатие на кнопку авторизации'):
            self.wait_for_clickable(loc.auth_button).click()
        notification_text = self.wait_for_visible(loc.notification).text
        with allure.step('Проверка текста ошибки'):
            assert notification_text == f"Не удалось авторизоваться: \"Пользователь с логином '{login}' не найден\""

    def auth_incorrect_password(self, login, password):
        with allure.step(f'Ввод логина "{login}"'):
            self.wait_for_visible(loc.login).send_keys(login)
        with allure.step(f'Ввод пароля "{password}"'):
            self.wait_for_visible(loc.password).send_keys(password)
        with allure.step('Нажатие на кнопку авторизации'):
            self.wait_for_clickable(loc.auth_button).click()
        notification_text = self.wait_for_visible(loc.notification).text
        with allure.step('Проверка текста ошибки'):
            assert notification_text == f'Не удалось авторизоваться: "Неверные учетные данные"'


    def auth_active_recovery_conf(self, login, password):
        with allure.step(f'Ввод логина "{login}"'):
            self.wait_for_visible(loc.login).send_keys(login)
        with allure.step(f'Ввод пароля "{password}"'):
            self.wait_for_visible(loc.password).send_keys(password)
        recovery_active = self.wait_for_visible(loc.recovery_conf_active)
        assert "ant-switch-checked" in recovery_active.get_attribute("class")
        # sleep(2)
        with allure.step('Нажатие на кнопку авторизации'):
            self.wait_for_clickable(loc.auth_button).click()

    def auth_inactive_recovery_conf(self, login, password):
        with allure.step(f'Ввод логина "{login}"'):
            self.wait_for_visible(loc.login).send_keys(login)
        with allure.step(f'Ввод пароля "{password}"'):
            self.wait_for_visible(loc.password).send_keys(password)
        recovery_active = self.wait_for_visible(loc.recovery_conf_active)
        with allure.step(f'Проверка, что кнопка активна'):
            assert "ant-switch-checked" in recovery_active.get_attribute("class")
#         sleep(2)
        with allure.step(f'Деактивация кнопки'):
            recovery_active.click()
        with allure.step(f'Проверка, что кнопка деактивирована'):
            assert "ant-switch-checked" not in recovery_active.get_attribute("class")
#         sleep(2)
        with allure.step('Нажатие на кнопку авторизации'):
            self.wait_for_clickable(loc.auth_button).click()

    def auth_correct_login_and_password(self, login, password):
        with allure.step(f'Ввод логина "{login}"'):
            self.wait_for_visible(loc.login).send_keys(login)
        with allure.step(f'Ввод пароля "{password}"'):
            self.wait_for_visible(loc.password).send_keys(password)
        with allure.step('Нажатие на кнопку авторизации'):
            self.wait_for_clickable(loc.auth_button).click()