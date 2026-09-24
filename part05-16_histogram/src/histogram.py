def histogram(my_str: str):
    alpha = {}
    for word in my_str:
        if word not in alpha:
            alpha[word] = word + " "
        if word in alpha[word]:
            alpha[word] += "*"
    for key in alpha:
        print(alpha[key])