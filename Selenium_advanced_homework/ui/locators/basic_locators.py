from selenium.webdriver.common.by import By


class BasePageLocators:
    SPINNER = (By.XPATH, '//div[contains(@class, "spinner") and not(@style)]')
    SEARCH_BY_TEXT = (By.XPATH, '//*[contains(text(), "{}")]')


class LoginPageLocators(BasePageLocators):
    LOGIN_BTN = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')


class NavBarLocators(BasePageLocators):
    AUDIENCE_BTN = (By.XPATH, '//a[@href="/segments"]')
    CAMPAIGN_BTN = (By.XPATH, '//a[@href="/dashboard"]')


class CampaignPageLocators(NavBarLocators):
    FIRST_CREATE_BTN = (By.XPATH, '//a[@href="/campaign/new"]')
    CREATE_BTN = (By.XPATH, '//div[contains(@class, "button-module-blue")]')
    CAMPAIGN_TITLE_PATTERN = (By.XPATH, '//a[@title="{}"]/../..')
    CAMPAIGN_SETTINGS_PATTERN = (By.XPATH, '//div[@data-row-id="{}"]//div[contains(@class, "icon-settings")]')
    DELETE_AD_BTN = (By.XPATH, '//li[@data-test="3"]')


class CreateCampaignPageLocators(NavBarLocators):
    TRAFFIC_BTN = (By.XPATH, '//div[contains(@class, "traffic")]')
    LINK_INPUT = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    ROUNDABOUT_TAB = (By.XPATH, '//div[contains(@id, "patterns_carousel")]')
    REMOVE_ATTACHMENTS_BTN = (By.XPATH, '//div[@data-test="button-remove-all"]')
    SLIDE_LINK_INPUT_TEMPLATE = (By.XPATH, '//input[@data-name="url_slide_{}"]')
    IMG_INPUT_600 = (By.XPATH, '//input[contains(@data-test, "image_600x600_slide")]')
    IMG_INPUT_600_BTN_GREEN = (By.XPATH, '//div[contains(@class, "roles-module-editButton")]/div[text()="600 × 600"]')
    SLIDE_TITLE_INPUT_TEMPLATE = (By.XPATH, '//input[@data-name="title_25_slide_{}"]')
    IMG_INPUT_256 = (By.XPATH, '//input[@data-test="icon_256x256"]')
    AD_TITLE_INPUT = (By.XPATH, '//input[@data-name="title_25"]')
    AD_TEXT_INPUT = (By.XPATH, '//textarea[@data-name="text_50"]')
    SLIDE_BTN_TEMPLATE = (By.XPATH, '//li[@data-id={}]')
    SAVE_AD_BTN = (By.XPATH, '//div[@data-test="submit_banner_button"]')
    CREATE_CAMPAIGN_BTN = (By.XPATH, '//div[contains(@class, "footer__button")]//button')
    CAMPAIGN_NAME_INPUT = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//input')


class AudiencePageLocators(NavBarLocators):
    CREATE_SEGMENT_BTN_FIRST = (By.XPATH, '//div[contains(@class, "page_segments__instruction-wrap") and'
                                          ' not(@style)]//a[@href="/segments/segments_list/new/"]'
                                )
    CREATE_SEGMENT_BTN = (By.XPATH, '//div[contains(@class, "segments-list__btn-wrap") and not(@style)]//button')
    SEGMENT_TITLE_TEMPLATE = (By.XPATH, '//a[@title="{}"]/../..')
    DELETE_SEGMENT_BTN_TEMPLATE = (By.XPATH, '//div[contains(@data-test, "remove") and @data-row-id="{}"]/span')
    DELETE_BTN = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')


class CreateSegmentPageLocators(NavBarLocators):
    SEGMENT_TYPE_TAB = (By.XPATH, '//div[contains(@class, "modal__block-left")]/div[8]')
    SEGMENT_TYPE_CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT_BTN = (By.XPATH, '//button[@data-class-name="Submit" and not(@disabled)]')
    SEGMENT_NAME_INPUT = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]//input')
    CREATE_SEGMENT_BTN = (By.XPATH, '//button[@data-class-name="Submit"]')
