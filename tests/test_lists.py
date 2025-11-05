import allure
import pytest

from pages.base_page import BasePage


class TestLists:

    @pytest.mark.lists
    def test_created_participant(self, auth, profiles_page, lists_page, configuration_page):
        name = profiles_page.create_profile()
        profiles_page.go_to_profile(name)
        configuration_page.go_to_lists_page()
        lists_page.create_participant()
        lists_page.got_to_back()
        profiles_page.delete_profile(name)

    def test_update_participant(self, auth, profiles_page, lists_page, configuration_page):
        name = profiles_page.create_profile()
        profiles_page.go_to_profile(name)
        configuration_page.go_to_lists_page()
        name_participant = lists_page.create_participant()
        lists_page.update_participant(name_participant)
        lists_page.got_to_back()
        profiles_page.delete_profile(name)