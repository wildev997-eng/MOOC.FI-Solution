let1 = input("1st letter:")
let2 = input("2nd letter:")
let3 = input("3rd letter:")

if let1 < let2 and let3 < let1:
    print(f"The letter in the middle is {let1}")
elif let1 > let2 and let3 > let1:
    print(f"The letter in the middle is {let1}")
elif let1 > let2 and let3 < let2:
    print(f"The letter in the middle is {let2}")
elif let1 < let2 and let3 > let2:
    print(f"The letter in the middle is {let2}")
elif let1 > let3 and let2 < let3:
    print(f"The letter in the middle is {let3}")
elif let1 < let3 and let2 > let3:
    print(f"The letter in the middle is {let3}")