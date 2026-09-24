layers = 3
size = 2 * layers - 1
center = size // 2
for r in range(size):
    row_string = ""
    for c in range(size):
        row_distance = abs(r - center)
        col_distance = abs(c - center)
        ring = max(row_distance, col_distance)
        row_string = chr(ord('A') + row_distance)
    print(row_string, end="")
