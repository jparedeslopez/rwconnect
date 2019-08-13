from .base import BasePage
from appium.webdriver.common.mobileby import MobileBy


class ContactEditPage(BasePage):

    # ===================
    # Inherited Constants
    # ===================
    driver = None
    logger = None

    # =========
    # Test Data
    # =========

    PHONE_NUMBER = "017582374945"

    # ========
    # Locators
    # ========

    PHONE_TEXT_FIELD = (MobileBy.ACCESSIBILITY_ID, "phone_text_field")
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, "Save")
    SUCCESS_OK = (MobileBy.ACCESSIBILITY_ID, "OK")
    BACK_HEADER = (MobileBy.ACCESSIBILITY_ID, "RWConnect.EditFriendTableView")
    BACK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="RWConnect"]')

    # ============
    # Page Methods
    # ============

    def get_phone_number(self):
        return self.get_element(self.PHONE_TEXT_FIELD).get_attribute("value")

    def enter_phone_number(self):
        box = self.get_element(self.PHONE_TEXT_FIELD)
        box.click()
        box.set_value(self.PHONE_NUMBER)
        self.get_element(self.SAVE_BUTTON).click()
        self.get_element(self.SUCCESS_OK).click()

    def back_to_home(self):
        self.get_element(self.BACK_BUTTON).click() #directly on test1?
