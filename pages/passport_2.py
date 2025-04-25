import logging

from locators.passport_locators import PassportLocators
from pages.base_page import BasePage

logger = logging.getLogger("qa")


class PassportPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_passport(self, name_text, last_name_text, date_text, about_text):
        logger.info(f"Try to add user with name {name_text}, last name {last_name_text}")
        self.fill(value=name_text, locator=PassportLocators.NAME)
        self.fill(value=last_name_text, locator=PassportLocators.LAST_NAME)
        self.fill(value=date_text, locator=PassportLocators.DATE)
        self.fill(value=about_text, locator=PassportLocators.ABOUT)
        self.click(locator=PassportLocators.SAVE_BUTTON)

    def get_table_text(self):
        return self.text(PassportLocators.USER_TABLE)