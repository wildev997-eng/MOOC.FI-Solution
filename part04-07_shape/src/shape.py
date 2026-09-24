def line(x: int, y: str):
    if y == "":
        y = "*"
        print(y * x)
    else :
        print(y[0] * x)

def shape(size1: int, character1: str, size2: int, character2: str):
    w = 0
    while w < size1:
        w += 1
        line(w, character1)
    z = 0
    while z < size2:
        z += 1
        line(size1, character2)

if __name__ == "__main__":
    shape(5, "x", 2, "o")