def formatted(x):
    z = []
    for grab in x:
        y = f"{grab:.2f}"
        z.append(y)
    return z

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)