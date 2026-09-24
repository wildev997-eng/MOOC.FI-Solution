def line(x: int, y: str):
    if y == "":
        y = "*"
        print(y * x)
    else :
        print(y[0] * x)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")