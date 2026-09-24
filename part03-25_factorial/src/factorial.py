while True:
    x = int(input("Please type in a number:"))
    y = 0
    z = 1

    if x <= 0:
        print("Thanks and bye!")
        break

    while y != x:
        y += 1
        z *= y
    
    print(f"The factorial of the number {x} is {z}")

