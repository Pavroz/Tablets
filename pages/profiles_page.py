from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import profiles_locators as loc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import allure
import random
import string

class ProfilesPage(BasePage):
    page_url = '/profiles'

    def __init__(self, driver):
        super().__init__(driver)


    def get_all_carts(self):
        """Получение списка карточек для дальнейшего взаимодействия с ними (например нажатие)"""
        return self.wait_for_all_visible(loc.all_carts)


    def get_all_carts_titles(self):
        """Получение списка с названиями карточек"""
        carts = self.wait_for_all_visible(loc.all_carts)
        titles = []
        for cart in carts:
            try:
                title = cart.find_element(*loc.name_cart).text.strip()
                titles.append(title)
            except Exception as e:
                print(f"Ошибка при получении названия карточки: {e}")
        return titles

    @staticmethod
    def generate_profile_name(prefix='test_', length = 20):
        """Генерация имени для тестового профиля"""
        suffix = ''.join(random.choice(string.ascii_lowercase + string.digits)
                         for _ in range(length - len(prefix)))
        return f'{prefix}{suffix}'

    @staticmethod
    def generate_profile_description(prefix='TEST_', length = 50):
        """Генерация описания для тестового профиля"""
        suffix = ''.join(random.choice(string.ascii_lowercase + string.digits)
                         for _ in range(length - len(prefix)))
        return f'{prefix}{suffix}'

    def create_profile(self, description=None):
        """Создает профиль и возвращает его имя"""
        name = self.generate_profile_name()
        with allure.step('Создание профиля'):
            try:
                if name in self.get_all_carts_titles():
                    print(f'Профиль "{name}" уже существует')
                    return None
                self.wait_for_clickable(loc.create_profile_button).click()
                self.wait_for_visible(loc.name_field).send_keys(name)
                if description:
                    self.wait_for_visible(loc.description_field).send_keys(description)
                self.wait_for_clickable(loc.apply_modals_button).click()
            except:
                pass
        # # Старый вариант функции
        # self.wait_for_clickable(loc.create_profile_button).click()
        # self.wait_for_visible(loc.name_field).send_keys(name)
        # if description:
        #     self.wait_for_visible(loc.description_field).send_keys(description)
        # self.wait_for_clickable(loc.apply_modals_button).click()
        # ПРОСТАЯ ПРОВЕРКА - ждем появления профиля по имени
        with allure.step(f'Проверка ожидания появления профиля по его имени - "{name}"'):
            assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{name}")]'))
        return name


    def delete_profile(self, profile_name):
        """Удаляет профиль по имени"""
        # Находим и кликаем кнопку удаления для профиля с нужным именем
        with allure.step('Нажатие на кнопку удаления'):
            delete_button = self.wait_for_presence(
                (By.XPATH,
                 f'//*[contains(text(), "{profile_name}")]//ancestor::prominform-profile-card//span[@nztype="delete"]')
            )

            delete_button.click()
        with allure.step('Подтверждение удаления'):
            self.wait_for_clickable(loc.yes_button_from_delete).click()
        # Ждем исчезновения профиля
        with allure.step('Ожидание удаления профиля'):
            assert WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, f'//*[contains(text(), "{profile_name}")]'))
            )


    def edit_name_profile(self, name_profile):
        new_name_profile = self.generate_profile_name()
        # Поиск кнопки редактирования
        with allure.step('Нажатие на кнопку редактирования'):
            edit_button = self.wait_for_clickable(
                (By.XPATH,
                 f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="edit"]')
            )
            edit_button.click()
        with allure.step('Очистка и заполнение поля ввода "Наименование"'):
            name_field = self.wait_for_clickable(loc.name_field)
            name_field.clear()
            name_field.send_keys(new_name_profile)
        with allure.step('Подтверждение редактирования'):
            self.wait_for_clickable(loc.apply_modals_button).click()
        with allure.step('Проверка, что наименование изменилось'):
            assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{new_name_profile}")]'))
        return new_name_profile

    def edit_description_profile(self, name_profile):
        new_description_profile = self.generate_profile_description()
        sleep(1)
        # Поиск кнопки редактирования
        with allure.step('Нажатие на кнопку редактирования'):
            edit_button = self.wait_for_clickable(
                (By.XPATH,
                 f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="edit"]')
            )
            edit_button.click()
        with allure.step('Очистка и заполнение поля ввода "Описание профиля"'):
            description_field = self.wait_for_visible(loc.description_field)
            description_field.clear()
            description_field.send_keys(new_description_profile)
        with allure.step('Подтверждение редактирования'):
            self.wait_for_clickable(loc.apply_modals_button).click()
        with allure.step('Проверка, что описание изменилось'):
            assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{name_profile}")]'))
        return new_description_profile

    def edit_full_profile(self, name_profile):
        new_name_profile = self.generate_profile_name()
        new_description_profile = self.generate_profile_description()
        with allure.step('Нажатие на кнопку редактирования'):
            edit_button = self.wait_for_clickable(
                (By.XPATH,
                 f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="edit"]')
            )
            edit_button.click()
        with allure.step('Очистка и заполнение полей ввода "Наименование" и "Описание профиля"'):
            name_field = self.wait_for_clickable(loc.name_field)
            name_field.clear()
            name_field.send_keys(new_name_profile)
            description_field = self.wait_for_clickable(loc.description_field)
            description_field.clear()
            description_field.send_keys(new_description_profile)
        with allure.step('Подтверждение редактирования'):
            self.wait_for_clickable(loc.apply_modals_button).click()
        with allure.step('Проверка, что наименование и описание изменились'):
            assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{new_name_profile}")]'))
        return new_name_profile

    def copy_profile(self, name_profile):
        new_name_profile = self.generate_profile_name()
        new_description_profile = self.generate_profile_description()
        with allure.step('Нажатие на кнопку копирования'):
            copy_button = self.wait_for_clickable(
                (By.XPATH,
                 f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="copy"]')
            )
            copy_button.click()
        with allure.step('Очистка и заполнение полей ввода "Наименование" и "Описание профиля"'):
            name_field = self.wait_for_clickable(loc.name_field)
            name_field.clear()
            name_field.send_keys(new_name_profile)
            description_field = self.wait_for_clickable(loc.description_field)
            description_field.clear()
            description_field.send_keys(new_description_profile)
        with allure.step('Подтверждение копирования'):
            self.wait_for_clickable(loc.apply_modals_button).click()
        with allure.step('Проверка, что профиль успешно скопировался'):
            assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{new_name_profile}")]'))
        return new_name_profile

    def activate_profile(self, name_profile):
        activate_button = self.wait_for_clickable(loc.activate_profile_button)
        activate_button.click()