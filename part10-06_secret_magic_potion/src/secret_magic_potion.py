# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name, passw: str):
        super().__init__(name)
        self.__passw = passw
    
    def add_ingredient(self, ingredient:str, amount:int, passw:str):
        if passw == self.__passw:
            self._ingredients.append((ingredient, amount))
        else:
            raise ValueError("Wrong password!")

    def print_recipe(self, password: str):
        if password == self.__passw:
            return super().print_recipe()
        else:
            raise ValueError("Wrong password!")
