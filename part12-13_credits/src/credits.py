from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(collect: list):
    return reduce(lambda total, attempt: total + attempt.credits, collect, 0)

def sum_of_passed_credits(collect: list):
    filtered = list(filter(lambda grading: grading.grade > 0, collect))
    return reduce(lambda total, attempt: total + attempt.credits, filtered, 0)

def average(collect: list):
    filtered = list(filter(lambda grading: grading.grade > 0, collect))
    grade_sum = reduce(lambda total, attempt: total + attempt.grade, filtered, 0)
    return grade_sum / len(filtered)