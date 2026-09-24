def row_correct(sudoku: list, row_no: int):
    not_repeating = True
    for index in sudoku[row_no]:
        if index != 0:
            check = sudoku[row_no].count(index)
            if check >= 2:
                not_repeating = False
                break
            elif check <= 1:
                not_repeating = True
    return not_repeating
