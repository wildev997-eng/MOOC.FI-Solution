si = input("Student information:")
ec = input("Exercises completed:")
ep = input("Exam points:")

def student_information():
    with open(si) as reading:
        si_container = {}
        for content in reading:
            begone = content.replace("\n", "")
            parts = begone.split(";")
            if parts[0] == "id":
                continue
            si_container[parts[0]] = " ".join(parts[1:])
        return si_container

def exercise_completed():
    with open(ec) as reading:
        ec_container = {}
        for content in reading:
            begone = content.replace("\n", "")
            parts = begone.split(";")
            if parts[0] == "id":
                continue
            ec_container[parts[0]] = parts[1:]
        for idd in ec_container:
            summ = 0
            for num in ec_container[idd]:
                summ += int(num)
            ec_container[idd] = summ
        return ec_container

def exam_points():
    with open(ep) as reading:
        ep_container = {}
        for content in reading:
            begone = content.replace("\n", "")
            parts = begone.split(";")
            if parts[0] == "id":
                continue
            ep_container[parts[0]] = parts[1:]
        for idd in ep_container:
            summ = 0
            for num in ep_container[idd]:
                summ += int(num)
            ep_container[idd] = summ
        return ep_container

def exercise_bonus():
    with open(ec) as reading:
        eb_container = {}
        for content in reading:
            begone = content.replace("\n", "")
            parts = begone.split(";")
            if parts[0] == "id":
                continue
            eb_container[parts[0]] = parts[1:]
        for idd in eb_container:
            summ = 0
            for num in eb_container[idd]:
                summ += int(num)
            bonus = (summ / 40) * 10
            eb_container[idd] = int(bonus)
        return eb_container

def grading():
    grading = {}
    call_eb = exercise_bonus()
    call_ep = exam_points()
    for idd, pts in call_eb.items():
        grading[idd] = pts
    for idd, pts in call_ep.items():
        grading[idd] = grading[idd] + int(pts)
    return grading

call_grd = grading()
call_eb = exercise_bonus()
call_si = student_information()
call_ep = exam_points()
call_ec = exercise_completed()

for printing in call_si:
    if call_grd[printing] >= 0 and call_grd[printing] <= 14:
        print(f"{call_si[printing]} 0")
    elif call_grd[printing] >= 15 and call_grd[printing] <= 17:
        print(f"{call_si[printing]} 1")
    elif call_grd[printing] >= 18 and call_grd[printing] <= 20:
        print(f"{call_si[printing]} 2")
    elif call_grd[printing] >= 21 and call_grd[printing] <= 23:
        print(f"{call_si[printing]} 3")
    elif call_grd[printing] >= 24 and call_grd[printing] <= 27:
        print(f"{call_si[printing]} 4")
    elif call_grd[printing] >= 28:
        print(f"{call_si[printing]} 5")
    