while True:
    x = input("Editor: ")
    x = x.lower()
    if x == "word" or x == "notepad":
        print("awful")
    elif x == "vscode" or x == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")