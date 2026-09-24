def count_matching_elements(my_matrix: list, element: int):
    e = element
    counter = 0
    for grab in my_matrix:
        for catch in grab:
            if catch == e:
                counter += 1

    return counter



