x = int(input("Limit:"))
z = 0
y = 1
c = ""

while z < x:
    if c == "":
        c += str(y)
    else:
        c += " + " + str(y)
    z += y
    y += 1 


print("The consecutive sum:", c, "=", z)