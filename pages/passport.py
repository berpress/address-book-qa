from selenium.webdriver.common.by import By


class PassportPage:
    def __init__(self, driver):
        self.driver = driver

    def add_passport(self, name_text, last_name_text, date_text, about_text):
        name = self.driver.find_element(By.ID, 'firstName')
        last_name = self.driver.find_element(By.ID, 'lastName')
        calendar = self.driver.find_element(By.ID, 'birthDate')
        about = self.driver.find_element(By.ID, 'about')
        btn_save = self.driver.find_element(By.XPATH,
                                       "//button[@data-test='submit-button']")
        name.send_keys(name_text)
        last_name.send_keys(last_name_text)
        calendar.send_keys(date_text)
        about.send_keys(about_text)
        btn_save.click()