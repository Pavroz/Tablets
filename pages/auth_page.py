from pages.base_page import BasePage
from pages.locators import auth_locators as loc
from time import sleep


class AuthPage(BasePage):
    page_url = '/auth'

    def auth_incorrect_login(self, login, password):
        self.wait_for_visible(loc.login).send_keys(login)
        self.wait_for_visible(loc.password).send_keys(password)
        self.wait_for_clickable(loc.auth_button).click()
        notification_text = self.wait_for_visible(loc.notification).text
        assert notification_text == f"Не удалось авторизоваться: \"Пользователь с логином '{login}' не найден\""

    def auth_incorrect_password(self, login, password):
        self.wait_for_visible(loc.login).send_keys(login)
        self.wait_for_visible(loc.password).send_keys(password)
        self.wait_for_clickable(loc.auth_button).click()
        notification_text = self.wait_for_visible(loc.notification).text
        assert notification_text == f'Не удалось авторизоваться: "Неверные учетные данные"'


    def auth_active_recovery_conf(self, login, password):
        self.wait_for_visible(loc.login).send_keys(login)
        self.wait_for_visible(loc.password).send_keys(password)
        recovery_active = self.wait_for_visible(loc.recovery_conf_active)
        assert "ant-switch-checked" in recovery_active.get_attribute("class")
        sleep(2)
        self.wait_for_clickable(loc.auth_button).click()

    def auth_inactive_recovery_conf(self, login, password):
        self.wait_for_visible(loc.login).send_keys(login)
        self.wait_for_visible(loc.password).send_keys(password)
        recovery_active = self.wait_for_visible(loc.recovery_conf_active)
        assert "ant-switch-checked" in recovery_active.get_attribute("class")
        sleep(2)
        recovery_active.click()
        assert "ant-switch-checked" not in recovery_active.get_attribute("class")
        sleep(2)
        self.wait_for_clickable(loc.auth_button).click()

    def auth_correct_login_and_password(self, login, password):
        self.wait_for_visible(loc.login).send_keys(login)
        self.wait_for_visible(loc.password).send_keys(password)
        self.wait_for_clickable(loc.auth_button).click()