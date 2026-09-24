def row_correct(sudoku: list):
    not_repeating_row = True
    for counting in range(len(sudoku)):
        for index in sudoku[counting]:
            if index != 0:
                check = sudoku[counting].count(index)
                if check >= 2:
                    not_repeating_row = False
                    break
                elif check <= 1:
                    not_repeating_row = True
        if not_repeating_row == False:
            return not_repeating_row
            break
    return not_repeating_row

def column_correct(sudoku: list):
    column = []
    catch = []
    i = 0
    not_repeating_column = True
    for counting in range(len(sudoku)):
        for index in sudoku:
            column.append(index[counting])
    while i < len(column):
        catch.append(column[i:i+9])
        i+=9
    for counting in range(len(catch)):
        for index in catch[counting]:
            if index != 0:
                check = catch[counting].count(index)
                if check >= 2:
                    not_repeating_column = False
                    break
                elif check <= 1:
                    not_repeating_column = True
        if not_repeating_column == False:
            return not_repeating_column
            break
    return not_repeating_column

def block_correct(sudoku: list):
    gridding = []
    merge_grid = []
    by_3 = []
    i = 0
    x = 0
    not_repeating_grid = True
    while x < len(sudoku):
        y = 0
        while y < len(sudoku):
            gridding.append(sudoku[y][x:x+3])
            y +=1
        x += 3
    for index in gridding:
        for element in index:
            merge_grid.append(element)
    while i < len(merge_grid):
        by_3.append(merge_grid[i:i+9])
        i += 9
    for counting in range(len(by_3)):
        for index in by_3[counting]:
            if index != 0:
                check = by_3[counting].count(index)
                if check >= 2:
                    not_repeating_grid = False
                    break
                elif check <= 1:
                    not_repeating_grid = True
        if not_repeating_grid == False:
            return not_repeating_grid
            break
    return not_repeating_grid

def sudoku_grid_correct(sudoku: list):
    rowwing = row_correct (sudoku)
    colummning = column_correct (sudoku)
    boxxing = block_correct (sudoku)
    
    if rowwing and colummning and boxxing:
        return True
    else:
        return False

def print_sudoku(sudoku: list):
    line = []
    regroup = []
    i = 0
    for index in sudoku:
        for element in index:
            if element == 0:
                element = "_"
            line.append(element)
    while i < len(line):
        regroup.append(line[i:i+9])
        i += 9

    for index in range(len(regroup)):
        for col in range(9):
            print(regroup[index][col], end=" ")
            if col == 2 or col == 5:
                print(" ", end="")
        print()
        if index == 2 or index == 5:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

