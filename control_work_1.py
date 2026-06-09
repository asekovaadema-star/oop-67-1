class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 
    
    def make_sound(self, sound):
        return 'какой то звук'

    @property 
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, new_age):
       if new_age<= 0 or new_age >= 25:
           raise ValueError ('Age is nonrealistic')
       self.__age = new_age

    @name.setter
    def name(self, new_name):
        self.__name = new_name
    

class Cat(Animal):
    def make_sound(self):
        return "мяу мяу"

class Dog(Animal):
    def make_sound(self):
        return "гав гав"
    
cat1 = Cat('Kitty', 5)
dog1= Dog('Nicolas II',10 )

print(cat1.age)
print(dog1.name)
print(dog1.make_sound())
print(cat1.make_sound())
