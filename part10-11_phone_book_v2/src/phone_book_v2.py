# Write your solution here:
class Person:
    def __init__(self, name: str):
        self._name = name
        self._numbers = []
        self._address = ""

    def name(self):
        return self._name

    def numbers(self):
        return self._numbers

    def address(self):
        if self._address == "":
            return None
        else:
            return self._address

    def add_number(self, number: str):
        self._numbers.append(number)

    def add_address(self, address: str):
        self._address = address

class PhoneBook :
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            new_person = Person(name)
            new_person.add_number(number)
            self.__persons[name] = new_person
        else:
            existing_person = self.__persons[name]
            existing_person.add_number(number)
    
    def add_address(self, name:str, address: str):
        if name not in self.__persons:
            new_person = Person(name)
            new_person.add_address(address)
            self.__persons[name] = new_person
        else:
            existing_person = self.__persons[name]
            existing_person.add_address(address)

    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        numbers = self.__persons[name].numbers()
        if numbers == []:
            return None
        return numbers

    def get_address(self,name:str):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        address = self.__phonebook.get_address(name)

        if address == None and numbers == None:
            print("address unknown")
            print("number unknown")
            return

        if address == None and numbers != None:
            for number in numbers:
                print(number)
            print("address unknown") 
            return

        if address != None and numbers == None:
            print("number unknown")
            print(address)
            return
        
        if address != None and numbers != None:
            for number in numbers:
                print(number)
            print(address)
            return

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))

# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions 
application = PhoneBookApplication()
application.execute()