def grade_input():
    grade_collect = []

    #This loop is for converting the string of user input into integer and store it
    while True:
        grade = input("Exam points and exercises completed:")
        if grade == "":
            break
        piece = grade.split(" ")
        numbers = []
        for grab in piece:
            numbers.append(int(grab))
        grade_collect.append(numbers)

    #This loop convert the exercise number into points of integer rounded down :)    
    conversion = []
    for grab in grade_collect:
        exe_point = grab[1] // 10
        grab[1] = exe_point 
        conversion.append(grab)

    #Returning the grade that's already converted into the next function
    return conversion

def grade_statistic(conversion: list):
    print("Statistics:")

    #Average grade loop and formula
    avg_idx = []
    for grab in conversion:
        summ = grab[0] + grab[1]
        avg_idx.append(summ)
    avg = sum(avg_idx)/len(avg_idx)
    print(f"Points average: {avg:.1f}")

    #Pass Percentage formula
    passing_grade = 0
    percent_hold = []
    for grab in conversion:
        if grab[0] >= 10:
            percent_hold.append(grab)
    for grab in percent_hold:
        if sum(grab) > 14:
            passing_grade += 1
    percentage = (passing_grade / len(conversion)) * 100
    print(f"Pass percentage:{percentage: .1f}")

    #Dot and pieces for visual
    grade0 = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    not_fail_exam = []
    for grab in conversion:
        if grab[0] < 10: 
            grade0 += 1
        else:
            not_fail_exam.append(grab)
    for grab in not_fail_exam:
        exam_sum = sum(grab)
        if exam_sum >= 28 and exam_sum <= 30:
            grade5 += 1
        elif exam_sum >= 24 and exam_sum <= 27:
            grade4 += 1
        elif exam_sum >= 21 and exam_sum <= 23:
            grade3 += 1
        elif exam_sum >= 18 and exam_sum <= 20:
            grade2 += 1
        elif exam_sum >= 15 and exam_sum <= 17:
            grade1 += 1
        else:
            grade0 += 1
    print("Grade distribution:")
    print(f"5: {grade5 * "*"}")
    print(f"4: {grade4 * "*"}")
    print(f"3: {grade3 * "*"}")
    print(f"2: {grade2 * "*"}")
    print(f"1: {grade1 * "*"}")
    print(f"0: {grade0 * "*"}")


grade = grade_input()
grade_statistic(grade)