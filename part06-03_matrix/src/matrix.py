def reading():
    with open("matrix.txt") as reading:
        container = []
        for content in reading:
            n = content.replace("\n", "")
            s = n.split(",")
            container.append(s)
        return container

def matrix_sum():
    call = reading()
    summ = 0
    for num in call:
        for add in num:
            summ += int(add)
    return summ

def matrix_max():
    call = reading()
    biggest = 0
    for num in call:
        maxx = max(num)
        biggest = max(biggest, int(maxx))
    return biggest

def row_sums():
    call = reading()
    row = []
    for num in call:
        rows = 0
        for summ in num:
            rows += int(summ)
        row.append(rows)
    return row