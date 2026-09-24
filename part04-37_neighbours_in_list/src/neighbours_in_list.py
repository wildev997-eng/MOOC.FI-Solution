def longest_series_of_neighbours(x: list):
    y = 0
    z = 0
    for g in range(len(x)-1):
        if x[g] - x[g+1] == -1 or x[g] - x[g+1] == 1:
            y += 1
            if y > z:
                z = y
        else:
            y = 0

    return z+1