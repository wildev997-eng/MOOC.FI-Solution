class Course:
    def __init__(self, course: str, grade: int, credit: int):
        self.__course = course
        self.__credit = credit
        self.__grade = grade
    
    def name(self):
        return self.__course
    
    def credit(self):
        return self.__credit
    
    def grade(self):
        return self.__grade
    
    def add_grade(self, new_grade: int):
        self.__grade = max(self.__grade, new_grade)
    
    def update_credit(self, new_cred):
        self.__credit = new_cred
    
    def __str__(self):
        return f"{self.__course} ({self.__credit} cr) grade {self.__grade}"

class CourseRecord:
    def __init__(self):
        self.__courses_dict = {}
    
    def add_course(self, course: str, grade: int, credit: int):
        if course not in self.__courses_dict:
            new_course = Course(course, grade, credit)
            self.__courses_dict[course] = new_course
        else:
            existing_course = self.__courses_dict[course]
            existing_course.add_grade(grade)
            existing_course.update_credit(credit)
    
    def printing_course(self, course):
        if course in self.__courses_dict:
            print(self.__courses_dict[course])
        else:
            print("no entry for this course")
    
    def printing_statistic(self):
        if self.__courses_dict == {}:
            print("There's no data")
        else:
            total_credits = 0
            total_grade = 0

            five = 0
            four = 0
            three = 0
            two = 0
            one = 0

            for course in self.__courses_dict.values():
                total_credits += course.credit()
                total_grade += course.grade()

                if course.grade() == 1:
                    one += 1
                elif course.grade() == 2:
                    two += 1
                elif course.grade() == 3:
                    three += 1
                elif course.grade() == 4:
                    four += 1
                else:
                    five += 1

            print(f"{len(self.__courses_dict)} completed courses, a total of {total_credits} credits")
            print(f"mean {total_grade / len(self.__courses_dict):.1f}")
            print("grade distribution")
            print(f"5: {"x" * five}")
            print(f"4: {"x" * four}")
            print(f"3: {"x" * three}")
            print(f"2: {"x" * two}")
            print(f"1: {"x" * one}")



class CourseApp:
    def __init__(self):
        self.__courseapp = CourseRecord()

    def add_course(self):
        course = input("course:")
        grade = int(input("grade:"))
        credit = int(input("credit:"))
        self.__courseapp.add_course(course, grade, credit)
    
    def printing(self):
        course = input("course:")
        self.__courseapp.printing_course(course)
    
    def statistic(self):
        self.__courseapp.printing_statistic()
    
    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistic")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.printing()
            elif command == "3":
                self.statistic()
            else:
                self.help()




application = CourseApp()
application.execute()