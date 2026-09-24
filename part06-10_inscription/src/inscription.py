name = input("Whom should i sign this to:")
file = input("Where shall i save it:")

with open(file, "w") as reading:
    reading.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")