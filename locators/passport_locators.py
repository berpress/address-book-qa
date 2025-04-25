from selenium.webdriver.common.by import By


class PassportLocators:
    NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    ABOUT = (By.ID, 'about')
    DATE = (By.ID, 'birthDate')
    SAVE_BUTTON =(By.XPATH,
                             "//button[@data-test='submit-button']")
    USER_TABLE = (By.ID, "userTable")
