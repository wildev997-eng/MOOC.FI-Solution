from math import sqrt
while True:
    x = int(input("Please type in a number:"))

    if x > 0:
        print(sqrt(x))
    elif x < 0:
        print("Invalid number")
    elif x == 0:
        break
print("Exiting...")