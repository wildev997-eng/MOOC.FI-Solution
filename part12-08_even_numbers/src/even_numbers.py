def even_numbers(beginning: int, maximum: int):
    if beginning % 2 == 1:
        beginning +=1
    
    while beginning <= maximum:
        yield beginning
        if beginning % 2 == 1:
            beginning +=1
        
        if beginning % 2 == 0:
            beginning += 2