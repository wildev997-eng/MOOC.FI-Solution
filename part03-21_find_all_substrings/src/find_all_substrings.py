x = input("Please type in a word:")
y = input("Please type in a character:")

while True:
    z = x.find(y)
    if len(x[z:(z+3)]) == 2:
        print("")
        break

    if len(x[z:(z+3)]) >= 3:
        print(x[z:(z+3)])
        x = x[(z+1):]
    else:
        print("")
        break