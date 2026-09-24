x = []

while True:
    y = int(input("New item: "))
    if y == 0:
        print("Bye!")
        break
    x.append(y)
    z = sorted(x)
    print(f"The list now: {x}")
    print(f"The list in order: {z}")