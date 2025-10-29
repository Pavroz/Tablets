import allure
import pytest


# name_profile = 'autotest'
# new_name_profile = 'АВТОТЕСТОВОЕ НАИМЕНОВАНИЕ ПРОФИЛЯ'
# new_description_profile = 'АВТОТЕСТОВОЕ ОПИСАНИЕ'

# ТЕСТЫ ПАРАЛЛЕЛИТЬ НА ДВА ОКНА

@allure.feature('Страница профилей')
class TestProfiles:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка создания профиля')
    @pytest.mark.profiles
    def test_create_profile(self, auth, profiles_page):
        name = profiles_page.create_profile()
        profiles_page.delete_profile(name)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка удаления профиля')
    @pytest.mark.profiles
    def test_delete_profile(self, auth, profiles_page):
        name = profiles_page.create_profile()
        profiles_page.delete_profile(name)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка изменения имени профиля')
    @pytest.mark.profiles
    def test_edit_name_profile(self, auth, profiles_page):
        name = profiles_page.create_profile()
        new_name_profile = profiles_page.edit_name_profile(name)
        profiles_page.delete_profile(new_name_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка изменения описания профиля')
    @pytest.mark.profiles
    def test_edit_description_profile(self, auth, profiles_page):
        name = profiles_page.create_profile()
        profiles_page.edit_description_profile(name)
        # sleep(2)
        profiles_page.delete_profile(name)

    @allure.story('Позитивные сценарии')
    @allure.title('Проферка изменения имени и описания профиля')
    @pytest.mark.profiles
    def test_edit_full_profile(self, auth, profiles_page):
        name = profiles_page.create_profile()
        new_name_profile = profiles_page.edit_full_profile(name)
        profiles_page.delete_profile(new_name_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проферка копирования профиля')
    @pytest.mark.profiles
    def test_copy_profile(self, auth, profiles_page):
        name = profiles_page.create_profile()
        new_name_profile = profiles_page.copy_profile(name)
        profiles_page.delete_profile(name)
        profiles_page.delete_profile(new_name_profile)