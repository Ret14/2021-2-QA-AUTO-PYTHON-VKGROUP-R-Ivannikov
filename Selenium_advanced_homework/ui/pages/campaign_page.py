import allure
from ui.locators import basic_locators
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.audience_page import AudiencePage
from ui.pages.base_page import BasePage


class CampaignPage(BasePage):

    locators = basic_locators.CampaignPageLocators
    ad_name = None

    @allure.step('Clicking on "Create campaign" button')
    def create_campaign(self):
        if self.elements_find(self.locators.FIRST_CREATE_BTN):
            self.click(self.locators.FIRST_CREATE_BTN)
        else:
            self.click(self.locators.CREATE_BTN)
        return CreateCampaignPage(driver=self.driver)

    @allure.step('Discarding a campaign')
    def delete_campaign(self):
        with allure.step('Composing a settings locator'):
            ad_title_locator = self.format_locator(self.locators.CAMPAIGN_TITLE_PATTERN, self.ad_name)
            row_attribute = self.find(ad_title_locator).get_attribute('data-row-id')
            settings_locator = self.format_locator(self.locators.CAMPAIGN_SETTINGS_PATTERN, row_attribute)
        self.click(settings_locator)
        self.click(self.locators.DELETE_AD_BTN)
        self.logger.info(f'Campaign "{self.ad_name}" is deleted')
        self.driver.refresh()

    @allure.step('Going to "audience page"')
    def go_to_audience_page(self):
        self.click(self.locators.AUDIENCE_BTN)
        self.spinner_wait()
        return AudiencePage(driver=self.driver)

