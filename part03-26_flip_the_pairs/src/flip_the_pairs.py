x = int(input("Please type in a number:"))
y = 0

while y < x:
    y += 1

    if y % 2 == 0:
        print(y-1)
    elif y % 2 != 0 and y != x:
        print(y+1)
    elif y == x and y % 2 != 0:
        print(y)
    
    
