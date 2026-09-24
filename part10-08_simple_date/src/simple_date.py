class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year
    
    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"
    
    def __combined(self):
        return self.__year * 10000 + self.__month * 100 + self.__date
    
    def __eq__(self, another):
        return self.__combined() == another.__combined()

    def __lt__(self, another):
        return self.__combined() < another.__combined()
    
    def __gt__(self, another):
        return self.__combined() > another.__combined()
    
    def __ne__(self, another):
        return self.__combined() != another.__combined()
    
    def __le__(self, another):
        return self.__combined() <= another.__combined()
    
    def __ge__(self, another):
        return self.__combined() >= another.__combined()

    def __add__(self, days):
        total_days = self.__year * 360 + (self.__month - 1) * 30 + (self.__date - 1)
        total_days += days

        new_year = total_days // 360
        remainder = total_days % 360
        new_month = remainder // 30 + 1
        new_date = remainder % 30 + 1

        return SimpleDate(new_date, new_month, new_year)
    
    def __sub__(self, another):
        tot_day1 = (self.__year * 360) + (self.__month * 30) + self.__date
        tot_day2 = (another.__year * 360) + (another.__month * 30) + another.__date
        return abs(tot_day1 - tot_day2)