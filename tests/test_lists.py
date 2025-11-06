import allure
import pytest

from pages.base_page import BasePage

@allure.feature('Страница списка участников')
class TestLists:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка создания участника')
    @pytest.mark.lists
    def test_created_participant(self, auth, profiles_page, lists_page, configuration_page):
        name = profiles_page.create_profile()
        profiles_page.go_to_profile(name)
        configuration_page.go_to_lists_page()
        lists_page.create_participant()
        lists_page.got_to_back()
        profiles_page.delete_profile(name)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка редактирования участника')
    @pytest.mark.lists
    def test_update_participant(self, auth, profiles_page, lists_page, configuration_page):
        name = profiles_page.create_profile()
        profiles_page.go_to_profile(name)
        configuration_page.go_to_lists_page()
        name_participant = lists_page.create_participant()
        lists_page.update_participant(name_participant)
        lists_page.got_to_back()
        profiles_page.delete_profile(name)
        ## Вариант с try - finally, чтобы профиль всегда удалялся
        # name = None
        # try:
        #     name = profiles_page.create_profile()
        #     profiles_page.go_to_profile(name)
        #     configuration_page.go_to_lists_page()
        #     name_participant = lists_page.create_participant()
        #     lists_page.update_participant(name_participant)
        #     # lists_page.got_to_back()
        # finally:
        #         try:
        #             lists_page.got_to_back()
        #             profiles_page.delete_profile(name)
        #         except Exception as e:
        #             print(f"Не удалось удалить профиль '{name}': {e}")