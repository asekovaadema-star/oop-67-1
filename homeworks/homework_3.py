class Person:
    def __init__(self, name, birth_date, occupation, higher_education=None):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    
    # @property
    # def age(self):

    @property
    def occupation(self):
        return self.__occupation
    
    @property
    def higher_education(self):
        if self.__higher_education:
            return 'У меня есть высшее образование'
        else:
            return 'У меня нет высшего образования'

    def introduce(self):
        print(f'Меня зовут {self.name}, я родилась {self.birth_date}, по профессии {self.occupation}, {self.higher_education}')

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name, higher_education):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
        
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я учусь с Адемой в {self.group_name} классе, родилась {self.birth_date}, работаю {self.occupation}, {self.higher_education}')
        
        
class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby, higher_education):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я подруга Адемы, родилась {self.birth_date}, работаю {self.occupation}, {self.higher_education}')

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory, higher_education):
        super().__init__(name, birth_date, occupation, hobby, higher_education)
        self.shared_memory = shared_memory
        
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я лучшая подруга Адемы, родилась {self.birth_date}, работаю {self.occupation}, {self.higher_education}')
        print(f'Вместе с Адемой мы {self.shared_memory}')


jasmin = BestFriend('Жасмин', '29.11.2009', 'мисс вселенной', 'пить колу', 'праздновали годовщину дружбы', True)
jasmin.introduce()

nurzhamal = Friend('Нуржамал', '01.10.2009', 'космонавтом', 'снимать видео', True)
ayana = Friend('Аяна', '12.08.2009', 'программистом', 'играть на комузе', True)

nurzhamal.introduce()
ayana.introduce()

bermet = Classmate('Бермет', '08.02.2009', 'судебно-медицинским экспертом', '10г', False)
aidemi = Classmate('Айдеми', '21.05.2009', 'бизнес-менеджером', '10г', False)

bermet.introduce()
aidemi.introduce()