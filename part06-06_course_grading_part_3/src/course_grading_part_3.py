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

def exercise_total():
    et_container = {}
    call_eb = exercise_bonus()
    call_ep = exam_points()
    for idd, pts in call_eb.items():
        et_container[idd] = pts
    for idd, pts in call_ep.items():
        et_container[idd] = et_container[idd] + int(pts)
    return et_container

def grading():
    grading = {}
    call_et = exercise_total()
    call_si = student_information()
    for printing in call_si:
        if call_et[printing] >= 0 and call_et[printing] <= 14:
            grading[printing] = 0
        elif call_et[printing] >= 15 and call_et[printing] <= 17:
            grading[printing] = 1
        elif call_et[printing] >= 18 and call_et[printing] <= 20:
            grading[printing] = 2
        elif call_et[printing] >= 21 and call_et[printing] <= 23:
            grading[printing] = 3
        elif call_et[printing] >= 24 and call_et[printing] <= 27:
            grading[printing] = 4
        elif call_et[printing] >= 28:
            grading[printing] = 5
    return grading

call_si = student_information()
call_ec = exercise_completed()
call_ep = exam_points()
call_eb = exercise_bonus()
call_et = exercise_total()
grd = grading()

print(f"{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}")
for printing in call_si:
    print(f"{call_si[printing]:<30}{call_ec[printing]:<10}{call_eb[printing]:<10}{call_ep[printing]:<10}{call_et[printing]:<10}{grd[printing]:<10}")