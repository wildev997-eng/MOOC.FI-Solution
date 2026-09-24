class BankAccount:
    def __init__(self, name : str, acc_num : str, balance: int):
        self.__name = name
        self.__acc_num = acc_num
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    def __service_charge(self):
        self.__balance = self.__balance - (self.__balance * 0.01)
        return self.__balance
        

    @property 
    def balance(self):
        return self.__balance
