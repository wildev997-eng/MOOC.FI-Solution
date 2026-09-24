def line(x: int, y: str):
    if y == "":
        y = "*"
        print(y * x)
    else :
        print(y[0] * x)


def square_of_hashes(size):
    z = 0
    while z < size:
        z += 1
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
