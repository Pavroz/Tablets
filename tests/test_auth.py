import pytest
import pytest
import os

@pytest.mark.skipif(os.getenv('CI'), reason="Internal site not accessible from CI")
@pytest.mark.auth
def test_incorrect_login(auth_page):
    auth_page.open()
    auth_page.auth_incorrect_login('qwe', '321')
@pytest.mark.skipif(os.getenv('CI'), reason="Internal site not accessible from CI")
@pytest.mark.auth
def test_incorrect_password(auth_page):
    auth_page.open()
    auth_page.auth_incorrect_password('0', 'qwe')
@pytest.mark.skipif(os.getenv('CI'), reason="Internal site not accessible from CI")
@pytest.mark.auth
def test_active_recovery_conf(auth_page):
    auth_page.open()
    auth_page.auth_active_recovery_conf('0', '321')
@pytest.mark.skipif(os.getenv('CI'), reason="Internal site not accessible from CI")
@pytest.mark.auth
def test_inactive_recovery_conf(auth_page):
    auth_page.open()
    auth_page.auth_inactive_recovery_conf('0', '321')
