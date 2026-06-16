class Backpack:
    def __init__(self, owner, items, max_items):
        self.owner = owner
        self.items = items
        self.max_items = max_items 
    
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Backpack owner: {self.owner}, items: {len(self.items)}, max_items: {self.max_items}"
    
    def __contains__(self, item):
        return item in self.items
    
    def __bool__(self):
        return bool(self.items)
    
    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
        else:
            print(f"Нельзя добавить {item}")
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Предмета {item} нет в рюкзаке")
    
backpack = Backpack("Азамат", ["ручка", "тетрадь"], 5)

print(backpack) 
print(len(backpack))

backpack.add_item("книга")
backpack.add_item("телефон")

print("книга" in backpack) 

backpack.remove_item("ручка")

if backpack:
    print("Рюкзак не пустой")
else:
    print("Рюкзак пустой")
