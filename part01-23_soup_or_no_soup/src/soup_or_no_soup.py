name = input("Please tell me your name:")
if name == "Jerry":
    print("Next please!")
if name != "Jerry":
    soup = int(input("How many portions of soup?"))
    print(f"The total cost is {soup*5.90}")
    print("Next please!")