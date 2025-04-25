import time


class TestPassport3:
    def test_passport_add_valid_data(self, passport_page_2):
        """
        1. Add valid data
        2. Check result
        """
        passport_page_2.add_passport(name_text='Иван',
                                   last_name_text='Петров',
                                   date_text='12.11.2000',
                                   about_text="Test QA")
        table_text = passport_page_2.get_table_text()
        assert "Иван" in table_text, "Пользователь не добавлен"

    def test_passport_add_minimal_name(self, passport_page_2):
        """
        1. Add valid data
        2. Check result
        """
        passport_page_2.add_passport(name_text='ЙЫ',
                                   last_name_text='Петров',
                                   date_text='12.11.2000',
                                   about_text="Test QA")
        table_text = passport_page_2.get_table_text()
        assert "ЙЫ" in table_text, "Пользователь не добавлен"


    def test_passport_invalid_name(self, passport_page_2):
        """
        1. Add valid data
        2. Check result
        """
        passport_page_2.add_passport(name_text='Ю',
                                   last_name_text='Петров',
                                   date_text='12.11.2000',
                                   about_text="Test QA")
        table_text = passport_page_2.get_table_text()
        assert "Ю" not in table_text, "Пользователь не добавлен"
