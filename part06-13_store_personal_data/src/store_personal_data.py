def store_personal_data(person: tuple):
    with open("people.csv", "a") as people:
        line = ""
        for index in person:
            line += f"{index};"
        line = line[:-1]
        people.write(line)
