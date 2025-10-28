from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import profiles_locators as loc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

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


    def create_profile(self, name, description=None):
        """Создает профиль и возвращает его имя"""
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
        assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{name}")]'))
        return name


    def delete_profile(self, profile_name):
        """Удаляет профиль по имени"""
        # Находим и кликаем кнопку удаления для профиля с нужным именем
        sleep(1)
        delete_button = self.wait_for_presence(
            (By.XPATH,
             f'//*[contains(text(), "{profile_name}")]//ancestor::prominform-profile-card//span[@nztype="delete"]')
        )
        delete_button.click()
        self.wait_for_clickable(loc.yes_button_from_delete).click()
        # Ждем исчезновения профиля
        assert WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, f'//*[contains(text(), "{profile_name}")]'))
        )


    def edit_name_profile(self, name_profile, new_name_profile):
        # Поиск кнопки редактирования
        edit_button = self.wait_for_clickable(
            (By.XPATH,
             f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="edit"]')
        )
        edit_button.click()
        name_field = self.wait_for_visible(loc.name_field)
        name_field.clear()
        name_field.send_keys(new_name_profile)
        self.wait_for_clickable(loc.apply_modals_button).click()
        assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{new_name_profile}")]'))


    def edit_description_profile(self, name_profile, new_description_profile):
        # Поиск кнопки редактирования
        edit_button = self.wait_for_clickable(
            (By.XPATH,
             f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="edit"]')
        )
        edit_button.click()
        description_field = self.wait_for_visible(loc.description_field)
        description_field.clear()
        description_field.send_keys(new_description_profile)
        self.wait_for_clickable(loc.apply_modals_button).click()
        # assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{name_profile}")]'))

    def edit_full_profile(self, name_profile, new_name_profile, new_description_profile=None):
        edit_button = self.wait_for_clickable(
            (By.XPATH,
             f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="edit"]')
        )
        edit_button.click()
        name_field = self.wait_for_visible(loc.name_field)
        name_field.clear()
        name_field.send_keys(new_name_profile)
        description_field = self.wait_for_visible(loc.description_field)
        description_field.clear()
        description_field.send_keys(new_description_profile)
        self.wait_for_clickable(loc.apply_modals_button).click()
        assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{new_name_profile}")]'))

    def copy_profile(self, name_profile, new_name_profile, new_description_profile=None):
        copy_button = self.wait_for_clickable(
            (By.XPATH,
             f'//*[contains(text(), "{name_profile}")]//ancestor::prominform-profile-card//span[@nztype="copy"]')
        )
        copy_button.click()
        name_field = self.wait_for_visible(loc.name_field)
        name_field.clear()
        name_field.send_keys(new_name_profile)
        description_field = self.wait_for_visible(loc.description_field)
        description_field.clear()
        description_field.send_keys(new_description_profile)
        self.wait_for_clickable(loc.apply_modals_button).click()
        assert self.wait_for_presence((By.XPATH, f'//*[contains(text(), "{new_name_profile}")]'))