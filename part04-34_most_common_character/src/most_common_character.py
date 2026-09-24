def most_common_character(x):
    y = sorted(list(x))
    w = ""
    z = 0
    if len(y) == 1 or len(y) <= 2:
        return y[-1]
    else:
        for grab in y:
            c = y.count(grab)
            if z < c:
                w = grab
                z = c
        return w