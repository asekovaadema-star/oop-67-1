class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я родилсялась {self.birth_date}, по профессии я {self.occupation}.")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        print(f"Меня зовут {self.name}, я учусь с Адемой в {self.group_name}. Моя профессия {self.occupation}.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    
    def introduce(self):
        print(f"Меня зовут {self.name}. Я подруга Адемы. Моя профессия {self.occupation}, мое хобби {self.hobby}.")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, hobby)
        self.shared_memory = shared_memory
    def introduce(self):
        super().introduce()
        print(f"Наше лучшее воспоминание: {self.shared_memory}.")


jasmin = BestFriend(name="Жасмин", birth_date="29.11.2009",occupation="мисс вселенной", hobby="пить колу", shared_memory="как мы праздновали годовщину дружбы")

jasmin.introduce()

bermet = Classmate("Бермет", "08.02.2009", "судебно-медицинский эксперт", "10Г класс")
aidemi = Classmate("Айдеми", "21.05.2009", "бизнес-менеджер", "10Г класс")

nurzhamal = Friend("Нуржамал", "01.10.2009", "космонавт", "снимать видео")
ayana = Friend("Аяна", "12.08.2009", "программист", "играть на комузе")

bermet.introduce()
aidemi.introduce()

nurzhamal.introduce()
ayana.introduce()


people_list = [bermet, ayana, jasmin]
for human in people_list:
    human.introduce()
    