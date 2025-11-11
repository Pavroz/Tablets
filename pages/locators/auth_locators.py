from selenium.webdriver.common.by import By



login = (By.CSS_SELECTOR, 'input[formcontrolname="login"]')
password = (By.CSS_SELECTOR, 'input[formcontrolname="password"]')
recovery_conf_active = (By.CSS_SELECTOR, '.ant-switch-checked')
auth_button = (By.CSS_SELECTOR, '.login-form-button')
notification = (By.CSS_SELECTOR, 'div.ant-notification-notice')

# Валидация при пустых полях ввода
# login_validation = (By.CSS_SELECTOR, 'nz-form-control[nzerrortip="Пожалуйста, введите логин!"]')
# password_validation = (By.CSS_SELECTOR, 'nz-form-control[nzerrortip="Пожалуйста, введите пароль!"]')
login_validation = (By.XPATH, '(//div[@role="alert"])[1]')
password_validation = (By.XPATH, '(//div[@role="alert"])[2]')
