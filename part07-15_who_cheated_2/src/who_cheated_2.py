def final_points():
    # name;task;points;hh:mm.
    import csv
    from datetime import datetime, timedelta
    
    with open("start_times.csv") as content:
        start = {}
        for line in csv.reader(content, delimiter=";"): 
            start[line[0]] = line[1]
    
    with open("submissions.csv") as content:
        ending = []
        for line in csv.reader(content, delimiter=";"):
            ending.append(line)

    non_cheater = []

    for name in start:
        timing_str = datetime.strptime(start[name], "%H:%M")
        for index in ending:
            timing_end = datetime.strptime(index[3], "%H:%M")
            if name == index[0] and timing_end - timing_str <= timedelta(hours=3) and index not in non_cheater:
                non_cheater.append(index)


    highest_grade = {}
    for index in non_cheater:
        task = {}
        task[index[1]] = index[2]
        if index[0] not in highest_grade:
            highest_grade[index[0]] = task
        
        if index[0] in highest_grade and index[1] not in highest_grade[index[0]]:
            highest_grade[index[0]].update(task)
        
        if index[0] in highest_grade and index[1] in highest_grade[index[0]] and int(index[2]) > int(highest_grade[index[0]][index[1]]):
                highest_grade[index[0]][index[1]] = index[2]

    summary = {}
    for index in highest_grade:
        total = 0
        for content in highest_grade[index]:
            total += int(highest_grade[index][content])
        summary[index] = total
    
    return summary

# {
#     'matti': 43, 
#     'erkki': 45, 
#     'antti': 41, 
#     'emilia': 42, 
#     'henrik': 37, 
#     'esko': 45, 
#     'kjell': 47, 
#     'jyrki': 41, 
#     'teemu': 43, 
#     'tiina': 36, 
#     'jenna': 38, 
#     'virpi': 39, 
#     'kalle': 46, 
#     'uolevi': 34,
#     'anna': 45, 
#     'kotivalo': 43, 
#     'justiina': 44, 
#     'matteus': 30, 
#     'markus': 35, 
#     'luukas': 40, 
#     'johannes': 39
#     }. 

# for index in non_cheater:
#     high = False
#     place = index
#     for content in non_cheater:
#         if place[0] == content[0] and place[1] == content[1] and int(content[2]) > int(place[2]):
#             place = content
#             high = True

#     if high and place not in highest_grade:
#         highest_grade.append(place)

 # summary = {}
    # for index in highest_grade:
    #     points = 0
    #     for content in highest_grade:
    #         if index[0] == content[0]:
    #             points += int(index[2])
    #     summary[index[0]] = points