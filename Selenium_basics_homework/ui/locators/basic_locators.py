from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.NAME, 'email')
PASSWORD_FIELD = (By.NAME, 'password')
LOGIN_BTN = (By.XPATH, '//div/div[contains(text(), "Войти")]')
ACCOUNT_TAB = (By.XPATH, '//div/span[@class="js-head-balance" and contains(text(), "0 ₽")]')
LOGOUT_TAB = (By.XPATH, '//div/ul/li[2]/a[@href="/logout"]')
PROFILE_BTN = (By.XPATH, '//li/a[@href="/profile"]')
NAME_FIELD = (By.XPATH, '//li/div/div[@data-name="fio"]/div/input')
PHONE_FIELD = (By.XPATH, '//li/div/div[@data-name="phone"]/div/input')
SAVE_BTN = (By.XPATH, '//div[@class="js-footer"]/button')
SPINNER = (By.XPATH, '//div[@class="spinner"]')
TOOLS_TAB = (By.XPATH, '//ul/li[7]/a[@href="/tools"]')
PRO_TAB = (By.XPATH, '//ul/li[5]/a[@href="/pro"]')
