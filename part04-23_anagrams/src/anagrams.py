def anagrams(x: str, y: str):
    z = sorted(x)
    w = sorted(y)

    if z[0:] == w[0:]:
        return True
    else:
        return False




if __name__ == "__main__":
    print(anagrams("tame", "meta"))