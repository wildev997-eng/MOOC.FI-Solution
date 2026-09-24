attempts = 1
while True:
    pin = input("PIN: ")
    if pin == "4321":
        break
    print("Wrong")
    attempts += 1
 
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")