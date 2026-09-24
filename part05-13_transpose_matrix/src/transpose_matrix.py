def transpose(matrix: list):
    i = 0
    gather = []
    box = []
    for index in matrix:
        for element in index:
            gather.append(element)
    while i < len(matrix):
        box.append(gather[i::len(matrix)])
        i += 1
    matrix.clear()
    matrix.extend(box)
