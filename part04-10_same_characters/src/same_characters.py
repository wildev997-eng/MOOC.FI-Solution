def same_chars(x: str, y: int, z: int):
    if y >= len(x) or z >= len(x):
        return False
    elif x[y] != x[z]:
        return False
    else:
        return True


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))