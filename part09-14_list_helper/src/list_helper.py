class  ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        freq = {}
        more = 0
        for index in my_list:
            tot = 0
            for counter in my_list:
                if index == counter:
                    tot += 1
            if index not in freq:
                freq[index] = tot
            else:
                pass
        
        for index, num in freq.items():
            more  = max(more, num)
        
        for index, num in freq.items():
            if more == num:
                return index
    
    @classmethod
    def doubles(cls, my_list: list):
        dubs = {}
        dubs_print = {}
        for index in my_list:
            tot = 0
            for counter in my_list:
                if index == counter:
                    tot += 1
            if index not in dubs:
                dubs[index] = tot
            else:
                pass
        for index, num in dubs.items():
            if num >= 2:
                dubs_print[index] = num
                
        return len(dubs_print)
