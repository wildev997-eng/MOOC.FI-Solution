while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function:"))

    if function == 1:
        fin = input("The word in Finnish:")
        eng = input("The word in English:")
        with open("dictionary.txt", "a") as over:
            over.write(f"{fin} - {eng} \n")
        print("Dictionary entry added")
    
    if function == 2:
        search = input("Search term:")
        compiling = []
        with open("dictionary.txt") as look:
            for index in look:
                index = index.strip()
                compiling.append(index)

            for content in compiling:
                if search in content:
                    print(content)
    
    if function == 3:
        print("Bye!")
        break