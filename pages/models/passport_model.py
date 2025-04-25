from faker import Faker
fake = Faker('ru_RU')

class PassportModel:
    def __init__(self, name=None, last_name=None, date=None, about=None):
        self.name=name
        self.last_name = last_name
        self.date = date
        self.about = about

    def random(self):
        name = fake.first_name()
        last_name = fake.last_name()
        date = "10.12.2000"
        about = fake.text()
        return PassportModel(name=name,
                             last_name=last_name,
                             date=date,
                             about=about)