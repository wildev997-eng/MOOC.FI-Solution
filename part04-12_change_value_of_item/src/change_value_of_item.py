x = [1, 2, 3, 4, 5]

while True:
    y = int(input("Index:"))

    if y < 0:
        break

    z = int(input("New Value:"))

    if y >=0:
        x[y] = z
        print(x)