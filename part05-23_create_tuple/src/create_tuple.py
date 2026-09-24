def create_tuple(x: int, y: int, z: int):
    place = x, y, z
    sort = sorted(place)
    x = min(sort)
    y = max(sort)
    z = sum(sort)
    return x,y,z


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))