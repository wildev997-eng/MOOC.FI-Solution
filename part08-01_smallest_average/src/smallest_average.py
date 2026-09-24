def smallest_average(person1: dict, person2: dict, person3: dict):
    p1 = 0
    p2 = 0
    p3 = 0

    for content in person1:
        if content == "name":
            continue
        p1 += int(person1[content])
    

    for content in person2:
        if content == "name":
            continue
        p2 += int(person2[content])
    
    for content in person3:
        if content == "name":
            continue
        p3 += int(person3[content])
    
    p1 = p1 / (len(person1) - 1)
    p2 = p2 / (len(person2) - 1)
    p3 = p3 / (len(person3) - 1)

    smallest = min(p1,p2,p3)

    if smallest == p1:
        return person1
    elif smallest == p2:
        return person2
    elif smallest == p3:
        return person3
        






# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
# print(smallest_average(person1, person2, person3))