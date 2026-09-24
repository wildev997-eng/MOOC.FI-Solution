def oldest_person(people: list):
    age = []
    for _,year in people:
        age.append(year)
    for index in people:
        if min(age) in index:
            return index[0]
            break
