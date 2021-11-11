from appium.webdriver.common.mobileby import MobileBy


class BaseLocators:
    TEXT_SEARCH = (MobileBy.XPATH, '//*[contains(@text, "{}")]')


class MainPageLocators(BaseLocators):
    KEYBOARD_BTN = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    RECORD_BTN = (MobileBy.XPATH, '//android.widget.FrameLayout[@resource-id='
                                  '"ru.mail.search.electroscope:id/assistant_voice_input_group"]'
                                  '//android.view.View')
    ABILITIES_TAB = (MobileBy.XPATH, '//*[contains(@text, "умеешь")]')

    SETTINGS_BTN = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')


class SearchPageLocators(BaseLocators):
    QUERY_INPUT = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    SEND_BTN = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_send')
    POPULATION_TAB = (MobileBy.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/suggests_list"]/*[6]')
    THUMB_UP_TAB = (MobileBy.XPATH, '//*[contains(@text, "👍")]')


class SettingsPageLocators(BaseLocators):
    NEWS_SOURCE_TAB = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    ABOUT_APP_TAB = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')


class NewsSourcesPageLocators(BaseLocators):
    NEWS_FM_TAB = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView//*[2]')
    CHECK_ELEM = (MobileBy.XPATH, '//*[@resource-id="ru.mail.search.electroscope:id/news_sources_item_selected"]')





