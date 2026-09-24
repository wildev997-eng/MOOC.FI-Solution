# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points1 = points * 1.1
    print("Your bonus is 10 %")
    print("You now have", points1, "points")

if points >= 100:
    points2 = points * 1.15
    print("Your bonus is 15 %")
    print("You now have", points2, "points")
