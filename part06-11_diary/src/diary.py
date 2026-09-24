while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function:"))
    if function == 1:
        with open("diary.txt", "a") as reading:
            reading.write(input("Diary Entry:") + "\n")
            print("Diary saved")
    
    if function == 2:
        with open("diary.txt") as reading:
            content = reading.read()
            print(content)
    
    if function == 0:
        print("Bye now!")
        break