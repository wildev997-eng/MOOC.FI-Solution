text = input("Write a text:")
# not edited one
splitter = text.split(" ")
big = splitter[:]

#lowc one
lowc = text.lower()
spliter = lowc.split(" ")
container = spliter[:]
x = 0

with open("wordlist.txt") as reading:
    content = reading.read()
    valid_words = content.split()
    for index in container:
        if index not in valid_words:
            big[x] = f"*{index}*"
        x += 1

merge = " ".join(big)
print(merge)
