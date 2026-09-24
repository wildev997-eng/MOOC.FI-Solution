def change_case(orig_string: str):
    spliting = orig_string.split(" ")
    morphed = []
    for index in spliting:
        line = ""
        for content in index:
            if content == content.lower():
                line += content.upper()
            
            if content == content.upper():
                line += content.lower()
        morphed.append(line)
    
    result = " ".join(morphed)
    return result

def split_in_half(orig_string: str):
    x = orig_string[0 : int(len(orig_string)/2)]
    y = orig_string[int(len(orig_string)/2):]
    z = (x,y)
    return z

def remove_special_characters(orig_string: str):
    import string
    spliting = orig_string.split(" ")
    morphed = []
    for index in spliting:
        line = ""
        for content in index:
            if content in string.ascii_lowercase or content in string.ascii_uppercase or content in string.digits:
                line += content
        morphed.append(line)

    result = " ".join(morphed)
    return result


    





# if __name__ == "__main__":
#     # x = change_case("Well hello there!")
#     # print(x)
#     # y = split_in_half("Well hello there!")
#     # print(y)
#     # w = remove_special_characters("Well hello there!")
#     # print(w)