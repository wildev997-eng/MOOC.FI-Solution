x = []
z = 0
while True:
    y = input("Word:")

    if y in x:
        print(f"You typed in {z} different words")
        break
    
    if y != x:
        z += 1
        x.append(y)