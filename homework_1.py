class Person:

    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'меня зовут {self.name}, я родилс в {self.birth_date}, по профессии {self.occupation}, высшее образование {self.higher_education}')


adema = Person('Адема', '10.06.2009', 'ученица', False)
jasmin = Person('Жасмин', '29.11.2009', 'ученица', False)
solarian = Person('Ian', '22.07.1654', 'voyager between words', True)

adema.introduce()
jasmin.introduce()
solarian.introduce()
