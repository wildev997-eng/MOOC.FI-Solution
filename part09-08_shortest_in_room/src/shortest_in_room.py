# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.room = []
        self.height = 0
    
    def add(self, person: Person):
        self.person = person
        self.room.append(self.person)
        self.height += self.person.height
    
    def is_empty(self):
        return len(self.room) == 0
    
    def print_contents(self):
        print(f"There are {len(self.room)} persons in the room, and their combined height is {self.height}")
        for index in self.room:
            print(f"{index.name} ({index.height} cm)")
    
    def shortest(self):
        if len(self.room) == 0:
            return None
        else:
            short = 0
            for index in self.room:
                if short == 0:
                    short = index.height
                
                short = min(short, index.height)

            for index in self.room:
                if short == index.height:
                    return index
    
    def remove_shortest(self):
        no_short = []
        shortie = ""
        self.height = 0
        if len(self.room) == 0:
            return None
        else:
            short = 0
            for index in self.room:
                if short == 0:
                    short = index.height
                
                short = min(short, index.height)
            
            for index in self.room:
                if short == index.height:
                    shortie = index
                    continue
                no_short.append(index)
                self.height += index.height

        self.room = no_short
        return shortie
        