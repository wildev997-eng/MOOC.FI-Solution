class LotteryNumbers:
    def __init__(self, week: str, lot: int):
        self.__week = week
        self.__lot = lot
    
    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.__lot])
    
    def hits_in_place(self, numbers: list):
        return [num if num in self.__lot else -1 for num in numbers]


