class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
    def introduce(self):
        print(f'меня зовут {self.name}, я родилась в {self.birth_date}, по профессии {self.occupation}')

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name
    def introduce(self, classmate_name):
        print(f'Привет, меня зовут {self.name}, я одноклассница {classmate_name}, родилась {self.birth_date}, работаю {self.occupation}')
        
        
class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby
    def introduce(self, friend_name):
        print(f'Привет, меня зовут {self.name}, я подруга {friend_name}, родилась {self.birth_date}, работаю {self.occupation}')

class BestFriend(Friend):
    def __init__(self,name, birth_date, occupation,hobby, shared_memory):
        super().__init__(name, birth_date, occupation, hobby)
        self.shared_memory = shared_memory
    def introduce(self,best_friend_name):
        print(f'Привет, меня зовут {self.name}, я лучшая подруга {best_friend_name}, родилась {self.birth_date}, работаю {self.occupation}')
        print(f'Вместе с {best_friend_name} я {self.shared_memory}')

jasmin = BestFriend('Жасмин', '29.11.2009', 'мисс вселенной','пить колу','праздновали годовщину дружбы')
jasmin.introduce('Адема')

nurzhamal = Friend('Нуржамал','01.10.2009', 'космонавтом','снимать видео')
ayana = Friend('Аяна', '12.08.2009', 'програмистом','играть на комузе' )

nurzhamal.introduce('Адемы')
ayana.introduce('Адема')


bermet = Classmate('Бермет', '08.02.2009', 'судебно-медицинский экспертом','10г класс')
aidemi = Classmate('Айдеми', '21.05.2009', 'бизнес менеджером','10г класс')

bermet.introduce('Адемы')
aidemi.introduce('Адемы')

people = [jasmin, ayana, aidemi]

for p in people:
    p.introduce()
    if not isinstance(p, BestFriend) and isinstance(p, Friend):
        print()



        



