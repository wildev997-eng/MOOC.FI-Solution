def everything_reversed(x):
    y = []
    for grab in x:
        z = grab[::-1]
        y.append(z)
    w = y[::-1]
    return w