def row_sums(my_matrix: list):
    holder = my_matrix[:]
    for index in holder:
        summ = 0
        for content in index:
            summ += content
        index.append(summ)
        my_matrix.append(index)
        my_matrix.pop(0)
