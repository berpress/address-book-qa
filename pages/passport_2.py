import logging

from locators.passport_locators import PassportLocators
from pages.base_page import BasePage
from pages.models.passport_model import PassportModel

logger = logging.getLogger("qa")


class PassportPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_passport(self, data: PassportModel):
        logger.info(f"Try to add user with name {data.name}, last name {data.last_name}")
        self.fill(value=data.name, locator=PassportLocators.NAME)
        self.fill(value=data.last_name, locator=PassportLocators.LAST_NAME)
        self.fill(value=data.date, locator=PassportLocators.DATE)
        self.fill(value=data.about, locator=PassportLocators.ABOUT)
        self.click(locator=PassportLocators.SAVE_BUTTON)

    def get_table_text(self):
        return self.text(PassportLocators.USER_TABLE)