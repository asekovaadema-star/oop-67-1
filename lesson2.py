#родительский класс, суперкласс 
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def drive_to(self, destination):
        print(f'Машина модели {self.model} едет в {destination}')
    
    def change_color(self, new_color):
        self.color = new_color
        

car_1 = Car('black', 'BMW')

car_1.drive_to('Karakol')
car_1.change_color('blue')

print(car_1.color)

#дочерний класс, ребенок, наслежник, подкласс 
class Bus(Car):
    def __init__(self,color, model, number ):
        super().__init__(color, model) #обращение к родительскому методу
        self.number = number

    def drive_to(self, destination):
        print(f'Автобус едет в {destination}')

bus_1 = Bus('yellow', 'Mercedec', '67sixseven')
print(bus_1.color)
bus_1.drive_to('Bishkek')


class Track(Car):
    def change_color(self, new_color):
        self.color = new_color
        print(f'цвет грузовика изменился на {new_color}')

track_1 = Track('silver', 'Bmw')

print(isinstance(bus_1, Bus)) #True
print(isinstance(bus_1, Car)) #True

vehicles = [car_1, bus_1, track_1]
for v in vehicles:
    v.drive_to('Karakol')

