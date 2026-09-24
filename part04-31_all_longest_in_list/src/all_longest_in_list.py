# = ["first", "second", "fourth", "eleventh"]
# = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

def all_the_longest(x):
    z = x[0]
    w = []
    for grab in x:
        y = str(grab)
        if len(y) > len(z):
            z = y
    w.append(z)
    for grab in x:
        y = str(grab)
        if len(w[0]) == len(y) and w[0] != y:
            w.append(y)
    return w
