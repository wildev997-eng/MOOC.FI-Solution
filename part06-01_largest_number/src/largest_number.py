def largest():
    with open("numbers.txt") as largest_num:
        larger = 0
        for num in largest_num:
            larger = max(larger, int(num))
        return larger
        