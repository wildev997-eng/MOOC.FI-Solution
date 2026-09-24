def length_of_longest(x: list):
    leng = 0
    for grab in x:
        y = str(grab)
        z = len(y)
        if z > leng:
            leng = z
    return leng

