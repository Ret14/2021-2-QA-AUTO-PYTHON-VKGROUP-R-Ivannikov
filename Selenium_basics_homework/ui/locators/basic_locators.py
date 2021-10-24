from selenium.webdriver.common.by import By

SPINNER = (By.XPATH, '//div[@class="spinner"]')

EMAIL_FIELD = (By.NAME, 'email')
PASSWORD_FIELD = (By.NAME, 'password')
LOGIN_BTN = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')

LOGOUT_TAB = (By.XPATH, '//a[@href="/logout"]')
PROFILE_BTN = (By.XPATH, '//a[@href="/profile"]')
TOOLS_BTN = (By.XPATH, '//a[@href="/tools"]')
PRO_BTN = (By.XPATH, '//a[@href="/pro"]')
ACCOUNT_TAB = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')

NAME_FIELD = (By.XPATH, '//div[@data-name="fio"]//input')
PHONE_FIELD = (By.XPATH, '//div[@data-name="phone"]//input')
SAVE_BTN = (By.XPATH, '//button')
