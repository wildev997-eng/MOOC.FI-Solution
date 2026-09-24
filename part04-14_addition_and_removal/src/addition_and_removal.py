x = []
y = 0
while True:
    print(f"The list is now {x}")
    z = input("a(d)d, (r)emove or e(x)it:")
    if z == "x":
        print("Bye!")
        break
    if z == "d":
        y += 1
        x.append(y)
    if z == "r":
        x.pop(-1)
        y -= 1
