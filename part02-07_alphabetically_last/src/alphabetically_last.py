nam1 = str(input("Please type in the 1st word:"))
nam2 = str(input("Please type in the 2nd word:"))

if nam1 < nam2:
    print(nam2, "comes alphabetically last.")
elif nam2 < nam1:
    print(nam1, "comes alphabetically last.")
else:
    print("You gave the same word twice.")