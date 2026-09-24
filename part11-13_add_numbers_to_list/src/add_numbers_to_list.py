def add_numbers_to_list(numbers: list):
    x = numbers[-1] + 1
    if len(numbers) % 5 != 0:
        numbers.append(x)
        add_numbers_to_list(numbers)
