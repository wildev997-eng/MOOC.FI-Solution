class Car:
    def __init__(self):
        self.__gas = 60
        self.__km = 0
    
    def fill_up(self):
        self.__gas = 60
    
    def drive(self, km:int):
        if km <= self.__gas:
            self.__gas -= km
            self.__km += km
        elif km > self.__gas:
            self.__km += self.__gas
            self.__gas = 0
        else:
            pass
      
    def __str__(self):
        return f"Car: odometer reading {self.__km} km, petrol remaining {self.__gas} litres"
