def block_correct(sudoku: list, row_no: int, column_no: int):
    by_3 = []
    not_repeating = True
    for index in sudoku[row_no:row_no+3]:
        for element in index[column_no:column_no+3]:
            by_3.append(element)

    for index in by_3:
        if index != 0:
            check = by_3.count(index)
            if check >= 2:
                not_repeating = False
                break
            elif check <= 1:
                not_repeating = True
    return not_repeating

