x = input("Please type in a string:")
y = input("Please type in a substring:")
z = x.find(y)

if z >= 0:
    z = x.find(y, (z + len(y)))
    if z != -1:
        print(f"The second occurrence of the substring is at index {z}.")
    if z == -1:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")