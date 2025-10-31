from selenium.webdriver.common.by import By

# Список профилей
all_carts = (By.TAG_NAME, "prominform-profile-card") # Весь список профилей
name_cart = (By.CSS_SELECTOR, ".profile-card__title span[nz-typography]") # Получение имени профиля

# get_all_profiles = (By.CSS_SELECTOR, 'div prominform-profile-card') # карточки профилей
# profile_name_in_card = (By.CSS_SELECTOR, 'span.ant-typography') # название внутри карточки

# Кнопки создания, редактирования, копирования и активации профиля
create_profile_button = (
    By.XPATH, '//span[contains(text(), "Создать профиль")]')
edit_profile_button = (By.CSS_SELECTOR, 'span[nztype="edit"]')
copy_profile_button = (By.CSS_SELECTOR, 'span[nztype="copy"]')
activate_profile_button = (By.CSS_SELECTOR, 'nz-switch[nzsize="small"]')

# Кнопка удаления профиля с подтверждением
delete_profile_button = (By.CSS_SELECTOR, 'span[nztype="delete"]')
yes_button_from_delete = (By.XPATH, '//span[contains(text(), "Да")]')

# Поля в модалке
name_field = (By.CSS_SELECTOR, 'input[formcontrolname="name"]')
description_field = (
    By.CSS_SELECTOR, 'textarea[formcontrolname="description"]')

# Подтверждение изменения
apply_modals_button = (
    By.CSS_SELECTOR, '.modal-footer button[nztype="primary"]')
# Отмена изменений
cancel_modals_button = (By.XPATH, '//span[text()="Отмена"]')