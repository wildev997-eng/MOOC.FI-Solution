def dict_of_numbers():
    x = 0
    num = {}
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen","twenty", "thirty",
            "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    for index in range(20):
        num[index] = ones[x]
        x += 1
    y = 0
    for index in range(20,30):
        if index == 20:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(30,40):
        if index == 30:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(40,50):
        if index == 40:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(50,60):
        if index == 50:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(60,70):
        if index == 60:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(70,80):
        if index == 70:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(80,90):
        if index == 80:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    y = 0
    x += 1
    for index in range(90,100):
        if index == 90:
            num[index] = ones[x]
        else:
            num[index] = ones[x] + "-" + ones[y]
        y += 1
    return num
