# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# URL = "https://berpress.github.io/ui-passport-demo/"
#
# @pytest.mark.skip
# class TestPassport:
#     def test_passport_add_valid_data(self):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         # открыть страницу
#         driver = webdriver.Chrome()
#         driver.get(URL)
#         #  находим элементы
#         name = driver.find_element(By.ID, 'firstName')
#         last_name = driver.find_element(By.ID, 'lastName')
#         calendar = driver.find_element(By.ID, 'birthDate')
#         about = driver.find_element(By.ID, 'about')
#         btn_save = driver.find_element(By.XPATH,
#                                        "//button[@data-test='submit-button']")
#         # действия
#         name.send_keys('Иван')
#         last_name.send_keys('Петров')
#         calendar.send_keys('12.12.2000')
#         about.send_keys('Test QA ABOUT')
#         btn_save.click()
#         time.sleep(4)
#         driver.quit()
#         pass
#     def test_passport_add_minimal_name(self):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         # открыть страницу
#         driver = webdriver.Chrome()
#         driver.get(URL)
#         #  находим элементы
#         name = driver.find_element(By.ID, 'firstName')
#         last_name = driver.find_element(By.ID, 'lastName')
#         calendar = driver.find_element(By.ID, 'birthDate')
#         about = driver.find_element(By.ID, 'about')
#         btn_save = driver.find_element(By.XPATH,
#                                        "//button[@data-test='submit-button']")
#         # действия
#         name.send_keys('Ив')
#         last_name.send_keys('Петров')
#         calendar.send_keys('12.12.2000')
#         about.send_keys('Test QA ABOUT')
#         btn_save.click()
#         time.sleep(4)
#         driver.quit()
#         pass
#     def test_passport_invalid_name(self):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         # открыть страницу
#         driver = webdriver.Chrome()
#         driver.get(URL)
#         #  находим элементы
#         name = driver.find_element(By.ID, 'firstName')
#         last_name = driver.find_element(By.ID, 'lastName')
#         calendar = driver.find_element(By.ID, 'birthDate')
#         about = driver.find_element(By.ID, 'about')
#         btn_save = driver.find_element(By.XPATH,
#                                        "//button[@data-test='submit-button']")
#         # действия
#         name.send_keys('И')
#         last_name.send_keys('Петров')
#         calendar.send_keys('12.12.2000')
#         about.send_keys('Test QA ABOUT')
#         btn_save.click()
#         time.sleep(4)
#         driver.quit()
#         pass