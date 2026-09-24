def no_shouting(x):
    y = []
    for grab in x:
        if grab.isupper() == False:
            y.append(grab)
    return y