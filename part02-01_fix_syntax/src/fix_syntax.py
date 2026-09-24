# Fix the program
number = int(input("Please type in a number:"))

if number > 100:
    print("The number was greater than one hundred")
    sub= number - 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", sub)
    print(sub, " must be my lucky number!")
    print("Have a nice day!")

if number < 100:
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")