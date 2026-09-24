def spruce(size):
    print("a spruce!")
    x = 0
    while x < size:
        x += 1
        y = (size - x) * " " #so this is the space before the stars. the firs t line has 4 spaces, the second line has 3 spaces, etc.
        z = (2 * x - 1) * "*" #so this is the number of stars. the first line has 1 star, the second line has 3 stars, etc.
        print(f"{y}{z}") # and this is the final print statement that prints the spaces and stars together to form the triangle shape.

    # Print the trunk
    trunk_space = (size - 1) * " " #this trunk space have the same formula as the space before the stars, but it is only printed once, so it is not in a loop.
    print(f"{trunk_space}*") #this print is just to call in the trunk space and print the trunk of the tree, which is just a single star.

if __name__ == "__main__":
    spruce(5)