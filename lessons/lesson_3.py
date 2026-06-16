class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False #защищен _что-то 
        self.__max_speed = 0 

    def __test(self):
        print(self.__max_speed) #только внутри класса , приватный 


    def _calcilate_fuel(self):
        print(self._fined)
        return 0
    
    def drive_to(self, destination):
        print(f'Машина модели {self.model} едет в {destination}')
    
    def change_color(self, new_color):
        self.color = new_color 
    
    def get_max_speed(self):
        return self.__max_speed
    
#getter 
    def get_max_speed(self):
        return self.__max_speed
#setter
    def set_max_speed(self, new_max_speed):
        if new_max_speed <= 0 or new_max_speed > 250:
            # print('max speed is nonrealistic')
            raise ValueError ('Max speed is nonreslistic')
        self.__max_speed =  new_max_speed

@property #decorator
def max_speed(self):
    #getter
    return self.__max_speed

@max_speed.setter
def max_speed(self, new_max_speed):
    if new_max_speed <= 0 or new_max_speed >= 250:
        raise ValueError ('Max speed is nonrealistic')
    self.__max_speed = new_max_speed 

car_1 = Car('black', 'BMW')

# car_1.drive_to('Karakol')

# car_1.change_color('blue')
# print(car_1.color)

# print(car_1.get_max_speed())
# # car_1.set_max_speed(-200)  #это вызовет ошибку
# car_1.set_max_speed(-200)
# print(car_1.get_max_speed())
# print('car is fined:' , car_1._fined)
# car_1.model =  'subaru'

# #print(car_1.__max_speed) #будет ошибка -- 5 приватному атрибуту 
# #print(car_1._Car__max_speed) #НЕЛЬЗЯ ТАК ОСТАВЛЯТЬ ИЛИ ДЕЛАТЬ 

# car_1.__max_speed = 20 #это бесполезная строка и ничего она не делает 
# car_1.drive_to ('Bishkek')