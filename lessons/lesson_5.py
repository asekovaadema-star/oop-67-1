#множественное наследование

class Animal:
    def move(self):
        print('animal is moving')

class Flying(Animal):
    def move(self):
        print('flying')
    
    def catch_meal(self):
        print('hunting food while flying')

class Swiming(Animal):
    def move(self):
        print('swiming')

class Duck(Flying, Swiming):
    def move(self):
        print('duck is swiming and flying')

duck = Duck()
duck.move()
#MRO - method resolution orded - порядок поиска метода
print(Duck.mro())
duck.catch_meal()

print(Flying.mro())