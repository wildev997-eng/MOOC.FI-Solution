def chessboard(x):
    y = 0
    while y < x:
        y+=1
        z=0
        while z < x:
            z+=1
            if z % 2 == 0 and y % 2 != 0:
                print("0", end="")
            elif z % 2 != 0 and y % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        print() 

# Testing the function
if __name__ == "__main__":
    chessboard(4)
