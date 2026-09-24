import difflib

text = input("Write a text: ")
# text = "this is acually a good and usefull program"
# not edited one
splitter = text.split(" ")
big = splitter[:]

#lowc one
lowc = text.lower()
spliter = lowc.split(" ")
container = spliter[:]
x = 0

with open("wordlist.txt") as reading:
    problematic = []
    content = reading.read()
    valid_words = content.split()
    for index in container:
        if index not in valid_words:
            big[x] = f"*{index}*"
            problematic.append(index)
        x += 1
    matches = {}
    for probs in problematic:
        matches[probs] = difflib.get_close_matches(probs, valid_words, 3)
    merge = " ".join(big)
    print(merge)
    print("suggestions:")
    for index in matches:
        line = ""
        for content in matches[index]:
            line += f"{content},"
        line = line[:-1]
        print(f"{index}: {line}")



#print(f"{probs}: {difflib.get_close_matches(probs, valid_words, 3).replace("'", "")}")
