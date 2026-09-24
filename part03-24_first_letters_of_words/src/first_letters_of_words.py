x = input("Please type in a sentence:")
y = " "
z = x.find(y)
print(x[0])

while z != -1:
    print(x[z + 1])
    z = x.find(y, (z + len(y)))




z = x.find(y, (z + len(y)))