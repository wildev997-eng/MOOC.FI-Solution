def read_fruits():
    with open("fruits.csv") as dictionary:
        fruit = {}
        container = []
        for content in dictionary:
            begone = content.replace("\n", "")
            spliting = begone.split(";")
            container.append(spliting)
        
        for content in container:
            fruit[content[0]] = content[1:]
        
        for content in fruit:
            for num in fruit[content]:
                fruit[content] = float(num)
        return fruit