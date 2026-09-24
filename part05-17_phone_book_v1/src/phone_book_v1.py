phone = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 1:
        name = input("Name:")
        for index in phone:
            if name == index:
                print(f"{phone[name]}")
        if name not in phone:
            print("no number")
    elif command == 2:
        name = input("Name:")
        number = input("Number:")
        phone[name] = number
        print("ok!")
    elif command == 3:
        print("quitting...")
        break