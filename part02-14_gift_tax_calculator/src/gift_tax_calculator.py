x = int(input("Value of gift:"))
cat1 = 100 + (x - 5000)*0.08
cat2 = 1700 + (x - 25000)*0.10
cat3 = 4700 + (x - 55000)*0.12
cat4 = 22100 + (x - 200000)*0.15
cat5 = 142100 + (x - 1000000)*0.17

if x < 5000:
    print("No tax!")

if x >= 5000 and x < 1000000:
    if x > 200000:
        print(f"Amount of tax: {cat4}")
    elif 2000000 > x > 55000:
        print(f"Amount of tax: {cat3}")
    elif 55000 > x > 25000:
        print(f"Amount of tax: {cat2}")
    elif 25000 > x > 5000:
        print(f"Amount of tax: {cat1}")
elif x > 1000000:
    print(f"Amount of tax: {cat5}")