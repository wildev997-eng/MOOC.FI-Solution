print("Please type in integer numbers. Type in 0 to finish.")
y = 0
z = 0
m = 0
p = 0
n = 0

while True:
    x = int(input("Numbers:"))

    if x == 0:
        count = True
    else:
        count = False

    if x > 0 and x != 0:
        p += 1
    elif x < 0:
        n += 1
    
    if count:
        break
    
    y += 1
    z += x
    m = z / y

print("... the program as for numbers")
print(f"Numbers typed in {y}")
print(f"The sum of the numbers is {z}")
print(f"The mean of the numbers is {m}")
print(f"Positive numbers {p}")
print(f"Negative numbers {n}")