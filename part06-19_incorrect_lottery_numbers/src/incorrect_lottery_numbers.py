def filter_incorrect():
    with open("lottery_numbers.csv") as scan:
        container = {}
        for index in scan:
            index = index.strip()
            strips = index.split(";")
            container[strips[0]] = strips[1:]

    with open("correct_numbers.csv", "w") as new_file:
        week = {}
        filter_length = {}
        not_same_number = {}
        string_filter = {}
        than = {}
        for index, num in container.items():
            week_co = True
            try:
                spliter = index.split(" ")
                numbering = int(spliter[1])
            except ValueError:
                week_co = False
            if week_co:
                week[index] = num
            
        for index, num in week.items():
            for element in num:
                spliting = element.split(",")
                week[index] = spliting
        
        for index, num in week.items():
            if len(num) == 7:
                filter_length[index] = num

        for index,num in filter_length.items():
            repeating = False
            for elemen in num:
                counting = num.count(elemen)
                if counting > 1:
                    repeating = True
            if not repeating:
                not_same_number[index] = num

        for index, num in not_same_number.items():
            weird = True
            for element in num:
                try:
                    inte = int(element)
                except ValueError:
                    weird = False
            if weird:
                string_filter[index] = num
        
        for index,num in string_filter.items():
            big = True
            for element in num:
                if int(element) > 39 or int(element) < 1:
                    big = False
            if big:
                than[index] = num
    
        lottery = []
        for index, name in than.items():
            data = []
            data.append(index)
            data.extend(name)
            lottery.append(data)

        for index in lottery:
            line = f"{index[0]};"
            for content in index:
                if "week" not in content:
                    line += f"{content},"
            line = line[:-1]
            new_file.write(line + "\n")
