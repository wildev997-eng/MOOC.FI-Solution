# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__total_cents = (euros * 100) + cents
        self.__printing = (self.__total_cents / 100)

    def __str__(self):
        return f"{self.__printing:.2f} eur"
    
    def __eq__(self, another):
        return self.__total_cents == another.__total_cents
    
    def __lt__(self, another):
        return self.__total_cents < another.__total_cents
    
    def __gt__(self, another):
        return self.__total_cents > another.__total_cents
    
    def __ne__(self, another):
        return self.__total_cents != another.__total_cents
    
    def __le__(self, another):
        return self.__total_cents <= another.__total_cents
    
    def __ge__(self, another):
        return self.__total_cents >= another.__total_cents
    
    def __add__(self, another):
        return f"{(self.__printing + another.__printing):.2f} eur"
    
    def __sub__(self, another):
        if self.__printing < another.__printing:
            raise ValueError("a negative result is not allowed")
        else:
            return f"{((self.__total_cents - another.__total_cents)/100):.2f} eur"
    
