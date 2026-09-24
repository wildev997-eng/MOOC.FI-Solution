class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list):
    return filter(lambda grade: grade.grade > 0, attempts)

def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda gradit: gradit.grade == grade, attempts)

def passed_students(attempts: list, course: str):
    course_name = list(filter(lambda crs_name: crs_name.course_name == course, attempts))
    passing_student = list(filter(lambda passing: passing.grade > 0, course_name))
    sorting = sorted(passing_student, key=lambda course: course.student_name)
    return (student.student_name for student in sorting)