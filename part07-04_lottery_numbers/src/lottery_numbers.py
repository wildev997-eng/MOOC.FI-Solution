def lottery_numbers(amount: int, lower: int, upper: int):
    from random import randint
    winning = []
    while len(winning) < amount:
        random = randint(lower, upper)
        if random not in winning:
            winning.append(random)
    return sorted(winning)

