def sum_of_positives(x: list):
    y = sorted(x)
    z = []
    for num in y:
        if num >= 0:
            z.append(num)
    
    w = sum(z)
    return w
