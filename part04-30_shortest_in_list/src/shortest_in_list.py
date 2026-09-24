def shortest(x: list):
    z = x[0]
    for grab in x:
        y = str(grab)
        if len(z) > len(y):
            z = y
        
    return z