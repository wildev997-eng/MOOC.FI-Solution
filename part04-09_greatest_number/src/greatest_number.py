def greatest_number(a, b, c):
    """
    This function takes three numbers as input and returns the greatest among them.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.
    
    Returns:
    int or float: The greatest number among the three inputs.
    """
    return max(a, b, c) # Max function is used to find the greatest number among the three inputs and the opposite is Min function which is used to find the smallest number among the three inputs.
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)