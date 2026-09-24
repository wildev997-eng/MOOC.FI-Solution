def generate_password(number: int):
    import string
    from random import sample

    x = string.ascii_lowercase
    password = "".join(sample(x, number))
    return password