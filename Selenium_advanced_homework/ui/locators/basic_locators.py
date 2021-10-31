from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BTN = (By.XPATH, '//div[text()="Войти"]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    WARNING_BLOCK = (By.XPATH, '//div[contains(@class, "notify-module-content")]')
    SPINNER = (By.XPATH, '//div[contains(@class, "spinner") and not(@style)]')


class NavBarLocators:
    AUDIENCE_BTN = (By.XPATH, '//a[@href="/segments"]')
    CAMPAIGN_BTN = (By.XPATH, '//a[@href="/dashboard"]')
    SPINNER = (By.XPATH, '//div[contains(@class, "spinner") and not(@style)]')


class CampaignPageLocators(NavBarLocators):
    FIRST_CREATE_BTN = (By.XPATH, '//a[@href="/campaign/new"]')
    CREATE_BTN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    CAMPAIGN_TITLE_PATTERN = (By.XPATH, '//a[@title="{}"]/../..')
    CAMPAIGN_SETTINGS_PATTERN = (By.XPATH, '//div[@data-row-id="{}"]//div[contains(@class, "icon-settings")]')
    DELETE_AD_BTN = (By.XPATH, '//li[@title="Удалить"]')


class CreateCampaignPageLocators(NavBarLocators):
    TRAFFIC_BTN = (By.XPATH, '//div[contains(@class, "traffic")]')
    LINK_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку"]')
    ROUNDABOUT_TAB = (By.XPATH, '//div[contains(@id, "patterns_carousel")]')
    REMOVE_ATTACHMENTS_BTN = (By.XPATH, '//div[@data-test="button-remove-all"]')
    SLIDE_LINK_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку для слайда"]')
    IMG_INPUT_600 = (By.XPATH, '//input[contains(@data-test, "image_600x600_slide")]')
    IMG_INPUT_600_BTN_GREEN = (By.XPATH, '//div[contains(@class, "roles-module-editButton")]/div[text()="600 × 600"]')
    SLIDE_TITLE_INPUT = (By.XPATH, '//input[@placeholder="Введите заголовок слайда"]')
    IMG_INPUT_256 = (By.XPATH, '//input[@data-test="icon_256x256"]')
    AD_TITLE_INPUT = (By.XPATH, '//input[@placeholder="Введите заголовок объявления"]')
    AD_TEXT_INPUT = (By.XPATH, '//textarea[@placeholder="Введите текст объявления"]')
    SLIDE_2_BTN = (By.XPATH, '//li[@data-id="1" ]')
    SLIDE_3_BTN = (By.XPATH, '//li[@data-id="2" ]')
    SLIDE_BTN_TEMPLATE = (By.XPATH, '//li[@data-id={}]')
    SAVE_AD_BTN = (By.XPATH, '//div[contains(text(), "Сохранить объявление")]')
    CREATE_CAMPAIGN_BTN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    CAMPAIGN_NAME_INPUT = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//input')


class AudiencePageLocators(NavBarLocators):
    CREATE_SEGMENT_BTN_FIRST = (By.XPATH, '//div[contains(@class, "page_segments__instruction-wrap") and'
                                          ' not(@style)]//a[@href="/segments/segments_list/new/"]'
                                )
    CREATE_SEGMENT_BTN = (By.XPATH, '//div[contains(@class, "segments-list__btn-wrap") and'
                                    ' not(@style)]//div[text()="Создать сегмент"]'
                          )
    SEGMENT_TITLE_TEMPLATE = (By.XPATH, '//a[@title="{}"]/../..')
    DELETE_SEGMENT_BTN_TEMPLATE = (By.XPATH, '//div[contains(@data-test, "remove") and @data-row-id="{}"]/span')
    DELETE_BTN = (By.XPATH, '//div[text()="Удалить"]')
    SEGMENT_NAME_TEMPLATE = (By.XPATH, '//*[text()="{}"]')


class CreateSegmentPageLocators(NavBarLocators):
    SEGMENT_TYPE_TAB = (By.XPATH, '//div[text()="Приложения и игры в соцсетях"]')
    SEGMENT_TYPE_CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT_BTN = (By.XPATH, '//div[text()="Добавить сегмент"]')
    SEGMENT_NAME_INPUT = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]//input')
    CREATE_SEGMENT_BTN = (By.XPATH, '//div[text()="Создать сегмент"]')

