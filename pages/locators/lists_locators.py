import os

from selenium.webdriver.common.by import By

# Создание, удаление и редактирование участника
create_button = (By.CSS_SELECTOR, '.anticon.anticon-plus')
edit_button = (By.CSS_SELECTOR, '.anticon.anticon-edit')

# Модалка создания/редактирования участника
lastname_field = (By.CSS_SELECTOR, 'input[formcontrolname="lastName"]')
firstname_field = (By.CSS_SELECTOR, 'input[formcontrolname="firstName"]')
middlename_field = (By.CSS_SELECTOR, 'input[formcontrolname="middleName"]')
subject_field = (By.CSS_SELECTOR, 'input[formcontrolname="county"]')
position_field = (By.CSS_SELECTOR, 'input[formcontrolname="position"]')
add_image_button = (By.CSS_SELECTOR, '.image-drag input[type="file"]')

# Кнопки создания и отмены
create_button_in_modal = (By.XPATH, '//span[text()="Создать "]')
save_button_in_modal = (By.XPATH, '//span[text()="Сохранить "]')
cancel_button_in_modal = (By.XPATH, '//span[text()="Отмена"]')
cross_button_in_modal = (By.CSS_SELECTOR, '.ant-modal-close-x')

# Удаление участника
delete_button = (By.CSS_SELECTOR, '.anticon.anticon-delete')
apply_delete_button = (By.CSS_SELECTOR, 'button[cdkfocusinitial="true"]')

# Взаимодействие с изображением
file_path = os.getcwd() + r'\data\image.png'