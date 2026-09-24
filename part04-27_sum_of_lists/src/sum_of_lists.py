def list_sum(x: list, y: list):
    w = 0
    index = []
    for z in x:
        t = z + y[w]
        w += 1
        index.append(t)

    return index