def separate_characters(my_string: str):
    import string

    lowup = string.ascii_letters
    pun = string.punctuation

    low_up = ""
    punctuation = ""
    mix = ""

    for char in my_string:
        if char in lowup:
            low_up += char
        
        if char in pun:
            punctuation += char
        
        if char not in lowup and char not in pun:
            mix += char

    tupling = (low_up, punctuation, mix)
    return tupling



    





# x = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(x)