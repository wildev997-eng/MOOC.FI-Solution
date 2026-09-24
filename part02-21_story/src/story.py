x = ""
y = ""
while True:
    story = input("Please type in a word: ")

    if story == "end" :
        word = True
    elif story == y :
        word = True
    else :
        word = False

    if word:
        break
    
    y = story
    x = x + " " + story



print(x)