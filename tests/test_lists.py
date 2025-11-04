import allure
import pytest



class TestLists:

    @pytest.mark.lists
    def test_created_participant(self, auth, profiles_page, lists_page, configuration_page):
        name = profiles_page.create_profile()
        profiles_page.go_to_profile(name)
        configuration_page.go_to_lists_page()
        lists_page.create_participant()
        profiles_page.delete_profile(name)