#абстракция 
from abc import ABC, abstractmethod
#абстрактынй класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass 
    @abstractmethod
    def test(self):
        pass
#конкретный класс
class Dog(Animal):
    def make_sound(self):
        print('woof-woof')
    def test(self):
        print('test in dog')
class Cat(Animal):
    def male_sound(self):
        print('meow-meow')
    def test(self):
        print('test in cat')

puppy = Dog()
puppy.make_sound()

#методы и переменные класса пайтон
class User:
    #атрибуты класса 
    user_count = 0 
    default_password = '123456789'

    def __init__(self, name, phone):
        self.name =  name
        self.phone = phone 
        self.role ='user'
        self.password = User.default_password
        User.user_count +=1 
    
    @classmethod
    def get_user_count(cls):
        return cls.user_count
    @classmethod
    def create_admin(cls, name, phone):
        user = cls(name, phone)
        user.role =  'admin'
        user.password = 'jdnnejdm101010'
        return user
    
    @staticmethod
    def validate_password(pswd):
        if len(pswd) < 8:
            return False
        return True
    
    def change_password(self, new_password):
        if not User.validate_password(new_password):
            raise ValueError('Password is short')
        self.password = new_password

print(User.user_count)
user1 = User('Adema', '996707691467')
print(user1.password)

admin1 = User.create_admin('Radomir', '996498985989')
print(admin1.password)
print(User.get_user_count())
print(f'всего пользователей: {User.user_count}')

user1.change_password('74638474368346')
print(User.validate_password('fcb'))