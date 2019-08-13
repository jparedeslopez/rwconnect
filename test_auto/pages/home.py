from .base import BasePage
from appium.webdriver.common.mobileby import MobileBy


class HomePage(BasePage):

    # ===================
    # Inherited Constants
    # ===================
    driver = None
    logger = None

    # =========
    # Test Data
    # =========

    MIC_TEXT = "Mic Pringle"

    # ========
    # Locators
    # ========

    FRIENDS = (MobileBy.ACCESSIBILITY_ID, "friends")
    INFO_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton')
    MIC = (MobileBy.ACCESSIBILITY_ID, MIC_TEXT)

    # ============
    # Page Methods
    # ============

    def open_info_button(self):
        friends_list = self.get_elements(self.FRIENDS)
        mic_element = None
        for friend in friends_list:
            if self.get_elements(locator=self.MIC, base_elem=friend):
                mic_element = friend
                break
        self.get_element(base_elem=mic_element, locator=self.INFO_BUTTON).click()

    def open_contact(self):
        friends_list = self.get_elements(self.FRIENDS)
        mic_element = None
        for friend in friends_list:
            if self.get_elements(locator=self.MIC, base_elem=friend):
                mic_element = friend
                break
        self.get_element(base_elem=mic_element, locator=self.MIC).click()
