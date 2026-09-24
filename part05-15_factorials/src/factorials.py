def factorials(n: int):
    factorial = {}
    start = 1
    for number in range(n + 1):
        if number > 0:
            factorial[number] = number * start
            start = number * start
    return factorial