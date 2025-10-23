import pytest
from time import sleep

name_profile = 'autotest'
new_name_profile = 'АВТОТЕСТОВОЕ НАИМЕНОВАНИЕ ПРОФИЛЯ'
new_description_profile = 'АВТОТЕСТОВОЕ ОПИСАНИЕ'

def test_create_profile(auth, profiles_page):
    profiles_page.create_profile(name_profile)
    profiles_page.delete_profile(name_profile)

def test_delete_profile(auth, profiles_page):
    profiles_page.create_profile(name_profile)
    profiles_page.delete_profile(name_profile)

def test_edit_name_profile(auth, profiles_page):
    profiles_page.create_profile(name_profile)
    profiles_page.edit_name_profile(name_profile, new_name_profile)
    profiles_page.delete_profile(new_name_profile)

def test_edit_description_profile(auth, profiles_page):
    profiles_page.create_profile(name_profile)
    profiles_page.edit_description_profile(name_profile, new_description_profile)
    # sleep(2)
    profiles_page.delete_profile(name_profile)