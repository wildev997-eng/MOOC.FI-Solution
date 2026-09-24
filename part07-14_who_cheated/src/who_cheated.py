def cheaters():
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
            
    cheater = []

    for name in start:
        cheat = False
        timing_str = datetime.strptime(start[name], "%H:%M")
        for index in ending:
            timing_end = datetime.strptime(index[3], "%H:%M")
            if name == index[0] and timing_end - timing_str > timedelta(hours=3):
                cheat = True
        if cheat:
            cheater.append(name)
    
    return cheater