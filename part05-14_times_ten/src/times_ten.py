def times_ten(start_index: int, end_index: int):
    multi ={}
    for index in range(start_index, end_index + 1):
        multi[index] = index * 10
    return multi