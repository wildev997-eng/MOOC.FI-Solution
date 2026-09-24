def line(x: int, y: str):
    if y == "":
        y = "*"
        print(y * x)
    else :
        print(y[0] * x)


def square(size, character):
    z = 0 
    while z < size:
        z += 1
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")