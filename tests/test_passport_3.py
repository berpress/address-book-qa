# import time
#
# import pytest
#
#
# @pytest.mark.skip
# class TestPassport3:
#     def test_passport_add_valid_data(self, passport_page):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         #  находим элементы
#         passport_page.add_passport(name_text='Иван',
#                                    last_name_text='Петров',
#                                    date_text='12.11.2000',
#                                    about_text="Test QA")
#         # time.sleep(4)
#
#     def test_passport_add_minimal_name(self, passport_page):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         passport_page.add_passport(name_text='Ив',
#                                    last_name_text='Петров',
#                                    date_text='12.11.2000',
#                                    about_text="Test QA")
#         # time.sleep(4)
#
#     def test_passport_invalid_name(self, passport_page):
#         """
#         1. Add valid data
#         2. Check result
#         """
#         passport_page.add_passport(name_text='И',
#                                    last_name_text='Петров',
#                                    date_text='12.11.2000',
#                                    about_text="Test QA")
#         # time.sleep(4)
