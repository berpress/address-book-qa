# import time
#
# import pytest
# from selenium import webdriver
#
# from pages.passport import PassportPage
#
# URL = "https://berpress.github.io/ui-passport-demo/"
#
# @pytest.mark.skip
# class TestPassport2:
#     def test_passport_add_valid_data(self):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         # открыть страницу
#         driver = webdriver.Chrome()
#         driver.get(URL)
#         #  находим элементы
#         passport_page = PassportPage(driver)
#         passport_page.add_passport(name_text='Иван',
#                                    last_name_text='Петров',
#                                    date_text='12.11.2000',
#                                    about_text="Test QA")
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
#         passport_page = PassportPage(driver)
#         passport_page.add_passport(name_text='Ив',
#                                    last_name_text='Петров',
#                                    date_text='12.11.2000',
#                                    about_text="Test QA")
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
#         passport_page = PassportPage(driver)
#         passport_page.add_passport(name_text='И',
#                                    last_name_text='Петров',
#                                    date_text='12.11.2000',
#                                    about_text="Test QA")
#         time.sleep(4)
#         driver.quit()
#         pass