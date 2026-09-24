def distinct_numbers(x: list):
    y = sorted(x)
    index = []
    for grab in y:
        if index == [] or grab != index[-1]:
            index.append(grab)
    return index

