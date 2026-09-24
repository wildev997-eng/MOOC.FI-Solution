def longest(strings: list):
    long = ""
    count = 0
    for grab in strings:
        if len(grab) > count:
            count = len(grab)
            long = grab
        
        if len(long) < len(grab):
            count = len(grab)
            long = grab

    return long


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))