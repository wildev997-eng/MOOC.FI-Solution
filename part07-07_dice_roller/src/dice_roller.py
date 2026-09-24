def roll(die: str):
    from random import shuffle

    A = [3,3,3,3,3,6]
    B = [2,2,2,5,5,5]
    C = [1,4,4,4,4,4]
    if die == "A":
        shuffle(A)
        roll = A[0]
        return roll
    
    if die == "B":
        shuffle(B)
        roll = B[0]
        return roll
    
    if die == "C":
        shuffle(C)
        roll = C[0]
        return roll

def play(die1: str, die2: str, times: int):
    d1 = 0
    d2 = 0
    t = 0
    for i in range(times):
        a = roll(die1)
        b = roll(die2)
        if a > b:
            d1 += 1
        if b > a:
            d2 += 1
        if a == b:
            t += 1
    tupling = (d1,d2,t)
    return tupling
