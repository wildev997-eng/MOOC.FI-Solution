def add_student(students: dict, add_name: str):
    students[add_name] = {'completed courses':[]}
    return students


def add_course(students: dict, name: str, course: str):
    if name in students:
        inner = students[name]['completed courses']
        repeating = False
        for index in range(len(inner)):
            if course[0] == inner[index][0]:
                repeating = True
                if course[1] > inner[index][1]:
                    repeating = True
                    inner[index] = course
        if not repeating and course[1] != 0:
            inner.append(course)


def print_student(students: dict, name: str):
    if name in students:
        inner = students[name]['completed courses']
        print(f"{name}:")
        if inner == []:
            print(" no completed courses")
        else:
            grade = []
            print(f" {len(inner)} completed courses:")
            for index in inner:
                print(f"  {index[0]} {index[1]}")
            for index in inner:
                grade.append(index[1])
            print(f" average grade {sum(grade) / len(inner)}")
    else:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    print(f"students {len(students)}")

    # most courses function
    course_num = []
    max_student = ""
    for index in students:
        course_num.append(len(students[index]['completed courses']))

    max_course = max(course_num)

    for index in students:
        if max_course == len(students[index]['completed courses']):
            max_student = index
    print(f"most courses completed {len(students[max_student]['completed courses'])} {max_student}")

    # best average grade
    grade = {}
    best_average = 0
    average_name = ""
    for name in students:
        place = []
        for element in students[name]['completed courses']:
            place.append(element[1])
        grade[name] = place
    for name in grade:
        summary = sum(grade[name]) / len(grade[name])
        grade[name] = summary
    for name in grade:
        if best_average< grade[name]:
            best_average = grade[name]
    for name in grade:
        if best_average == grade[name]:
            average_name = name
    print(f"best average grade {best_average} {average_name}")