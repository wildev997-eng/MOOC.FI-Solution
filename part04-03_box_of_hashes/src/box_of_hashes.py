def line(x: int, y: str):
    if y == "":
        y = "*"
        print(y * x)
    else :
        print(y[0] * x)

def box_of_hashes(height):
    z = 0
    while z < height:
        z += 1
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
