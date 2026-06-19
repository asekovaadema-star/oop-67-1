class Hero:

    def __init__(self, name, lvl, hp):
        #конструктор класса
        self.hero_name =  name 
        self.hero_lvl = lvl
        self.hero_hp = hp
    
    #это метод класса а не функции
    def action(self):
        print(f'{self.hero_name}Base action!!!')
    
    def rest(self):
        print(f'{self.hero_name} rest!!!')

kirito = Hero('Kirito', 100, 1000)
asuma = Hero('asuma', 99, 999)

#HeroMage - толко для классов
#hero_kirito - все остальное 

#def __init__(self): 
#это конструктор 
