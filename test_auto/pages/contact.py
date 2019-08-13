from .base import BasePage
from appium.webdriver.common.mobileby import MobileBy
from .contact_edit import ContactEditPage


class ContactPage(BasePage):

    # ===================
    # Inherited Constants
    # ===================
    driver = None
    logger = None

    # =========
    # Test Data
    # =========

    # ========
    # Locators
    # ========

    MAIN_PHONE = (MobileBy.XPATH, '//XCUIElementTypeCell[@name="main"]')

    # ============
    # Page Methods
    # ============

    def find_phone_number(self):
        stored_phone = self.get_element(self.MAIN_PHONE)
        return int(stored_phone.text.encode('ascii','ignore'))
