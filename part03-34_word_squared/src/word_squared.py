def squared(x, y):
    z = 0
    while z < y:
        r = 0
        while r < y:
            i = (z*y+r) % len(x)
            if r % 2 == 0:
                print(x[i], end="")
            else:
                print(x[i], end="")
            r += 1
        print()
        z += 1

if __name__ == "__main__":
    squared("aybabtu", 5)