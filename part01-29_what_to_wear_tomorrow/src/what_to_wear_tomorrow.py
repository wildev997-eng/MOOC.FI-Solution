print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature:"))
rain = input("Will it rain (yes/no):")
if temp <= 25:
        print("Wear jeans and a T-shirt")
if temp <= 20:
        print("I recommend a jumper as well")
if temp <=10:
        print("Take a jacket with you")
if temp <= 5:
        print("I think gloves are in order")
        print("Make it a warm coat, actually")
if rain == "yes":
        print("Don't forget your umbrella!")