x = float(input("Hourly wage:"))
y = int(input("Hours worked:"))
day = input("Day of the week:")
if day == "Sunday":
    print(f"Daily wages: {(x*2)*y} euros")
if day != "Sunday":
    print(f"Daily wages: {x*y} euros")