def recursive_sum(number: int):
    if number <= 1:
        return number

    num_below = recursive_sum(number - 1)
    sum_tot = num_below + number
    return sum_tot
