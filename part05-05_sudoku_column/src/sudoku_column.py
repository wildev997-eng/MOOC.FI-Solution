def column_correct(sudoku: list, column_no: int):
    catch = []
    not_repeating = True
    for index in sudoku:
        catch.append(index[column_no])

    for index in catch:
        check = catch.count(index)
        if index != 0:
            check = catch.count(index)
            if check >= 2:
                not_repeating = False
                break
            elif check <= 1:
                not_repeating = True
    return not_repeating