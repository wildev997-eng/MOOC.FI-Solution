x = int(input("Year"))
l = x + 1
 
while True :
    if l % 400 == 0:
        leap = True
    elif l % 100 == 0:
        leap = False
    elif l % 4 == 0:
        leap = True
    else:
        leap = False
    
    if leap :
        break
    l = l + 1

print(f"The next leap year after {x} is {l}")