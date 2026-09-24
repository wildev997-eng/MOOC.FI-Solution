def invert(dictionary: dict):
    revert = {}
    for key in dictionary:
        revert[dictionary[key]] = key
    dictionary.clear()
    dictionary.update(revert)