class Recording:
    def __init__(self, leng):
        self.length = leng
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, leng: int):
        if leng < 0:
            raise ValueError("The amount must not be below zero")
        else:
            self.__length = leng
