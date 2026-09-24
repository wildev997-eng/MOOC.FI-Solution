grade = int(input("How many points[0-100]:"))

if grade < 0 or grade >= 101:
    print("Grade: impossible!")
elif grade <= 100 and grade >= 90:
    print("Grade: 5")
elif grade < 90 and grade >= 80:
    print("Grade: 4")
elif grade < 80 and grade >= 70:
    print("Grade: 3")
elif grade < 70 and grade >= 60:
    print("Grade: 2")
elif grade < 60 and grade >=50:
    print("Grade: 1")
elif grade < 50 and grade >=0:
    print("fail")