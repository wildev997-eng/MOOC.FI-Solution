class Person:
    def __init__(self, name:str):
        self.name = name

    def return_first_name(self):
        spacing = self.name.find(" ")
        first = self.name[:spacing]
        return first


    def return_last_name(self):
        spacing = self.name.find(" ")
        last = self.name[(spacing+1):]
        return last

if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())
















