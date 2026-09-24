class Item:
    def __init__(self, name: str, weight: int):
        self.set_name(name)
        self.set_weight(weight)

    def name(self):
        return self.__name

    def set_name(self, name):
        if name == "":
            raise ValueError
        else:
            self.__name = name

    def weight(self):
        return self.__weight

    def set_weight(self, weight):
        if weight < 0:
            raise ValueError
        else:
            self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, weight: int):
        self.max_weight = weight
        self.__load = 0
        self.__cont = []
    
    def add_item(self, item: Item):
        if item.weight() + self.__load > self.max_weight:
            pass
        else:
            self.__cont.append(item)
            self.__load += item.weight()

    def print_items(self):
        for index in self.__cont:
            print(f"{index.name()} ({index.weight()} kg)")
    
    @property
    def content(self):
        return self.__cont

    def weight(self):
        return self.__load

    def heaviest_item(self):
        if len(self.__cont) == 0:
            return None
        else:
            heavy = 0
            for index in self.__cont:
                heavy = max(heavy, index.weight())
            for index in self.__cont:
                if index.weight() == heavy:
                    return index

    def __str__(self):
        if len(self.__cont) == 1:
            return f"{len(self.__cont)} item ({self.__load} kg)"
        else:
            return f"{len(self.__cont)} items ({self.__load} kg)"
            

class CargoHold:
    def __init__(self, cargo_weight:int):
        self.cargo_weight = cargo_weight
        self.__cargo_load = 0
        self.__cargo_cont = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__cargo_load > self.cargo_weight:
            pass
        else:
            self.__cargo_cont.append(suitcase)
            self.__cargo_load += suitcase.weight()
    
    def print_items(self):
        for index in self.__cargo_cont:
            for item in index.content:
                print(item)
            
    
    def __str__(self):
        if len(self.__cargo_cont) == 1:
            return f"{len(self.__cargo_cont)} suitcase, space for {self.cargo_weight - self.__cargo_load} kg"
        else:
            return f"{len(self.__cargo_cont)} suitcases, space for {self.cargo_weight - self.__cargo_load} kg"


# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# adas_suitcase = Suitcase(10)
# adas_suitcase.add_item(book)
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(10)
# peters_suitcase.add_item(brick)

# cargo_hold = CargoHold(1000)
# cargo_hold.add_suitcase(adas_suitcase)
# cargo_hold.add_suitcase(peters_suitcase)

# print("The suitcases in the cargo hold contain the following items:")
# cargo_hold.print_items()