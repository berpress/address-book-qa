from pages.models.passport_model import PassportModel


class TestPassport3:
    def test_passport_add_valid_data(self, passport_page_2):
        """
        1. Add valid data
        2. Check result
        """
        data = PassportModel().random()
        passport_page_2.add_passport(data=data)
        table_text = passport_page_2.get_table_text()
        assert data.name in table_text, "Пользователь не добавлен"

    def test_passport_add_minimal_name(self, passport_page_2):
        """
        1. Add valid data
        2. Check result
        """
        data = PassportModel().random()
        data.name = 'ЙЫ'
        passport_page_2.add_passport(data=data)
        table_text = passport_page_2.get_table_text()
        assert data.name in table_text, "Пользователь не добавлен"


    def test_passport_invalid_name(self, passport_page_2):
        """
        1. Add valid data
        2. Check result
        """
        data = PassportModel().random()
        data.name = 'Ю'
        passport_page_2.add_passport(data=data)
        table_text = passport_page_2.get_table_text()
        assert data.name not in table_text, "Пользователь не добавлен"
