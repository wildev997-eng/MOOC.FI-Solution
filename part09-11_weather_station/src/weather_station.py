class WeatherStation:
    def __init__(self, city:str):
        self.__city = city
        self.__numobs = 0
        self.__weather = ""

    def add_observation(self, observation: str):
        self.__weather = observation
        self.__numobs += 1

    def latest_observation(self):
        return self.__weather
    
    def number_of_observations(self):
        return self.__numobs

    def __str__(self):
        return f"{self.__city}, {self.__numobs} observations"



