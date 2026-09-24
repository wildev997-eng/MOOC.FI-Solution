def palindromes(x: str):
    y = x[::-1]
    if y == x:
        return True
    else:
        return False

while True:
    word = input("Please type in a palindrome:")
    if palindromes(word) == True:
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")