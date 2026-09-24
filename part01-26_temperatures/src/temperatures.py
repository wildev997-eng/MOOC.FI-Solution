x = int(input("Please type in a temperature (F):"))
c = (x-32)/1.8
if c >= 0:
    print(f"{x} degrees Fahrenheit equals {c} degrees Celsius")
if c < 0:
    print(f"{x} degrees Fahrenheit equals {c} degrees Celsius")
    print("Brr! It's cold in here!")