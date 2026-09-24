def older_people(people: list, year: int):
    older = []
    names = []
    for _, years in people:
        if years < year:
            older.append(years)

    for index in older:
        for name,years in people:
            if index == years:
                names.append(name)
            
    return names