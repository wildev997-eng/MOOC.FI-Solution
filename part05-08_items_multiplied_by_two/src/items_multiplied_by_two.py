def double_items(numbers: list):
    doubled = []
    for index in numbers:
        two = index * 2
        doubled.append(two)
    return doubled


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)