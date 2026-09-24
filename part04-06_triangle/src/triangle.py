def line(x: int, y: str):
    if y == "":
        y = "*"
        print(y * x)
    else :
        print(y[0] * x)


def triangle(size):
    z = 0
    while z < size:
        z += 1
        line(z, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
