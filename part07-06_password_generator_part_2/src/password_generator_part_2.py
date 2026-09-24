def generate_strong_password(number: int, condition1: bool, condition2: bool):
    import string

    from random import sample

    l = string.ascii_lowercase
    n = string.hexdigits
    m = "!?=+-()#"

    if condition1 is False and condition2 is False:
        password = "".join(sample(l, number))
        return password

    if condition1 is True and condition2 is False:
        password = "".join(sample(n, number))
        password = password.lower()
        return password

    if condition1 is False and condition2 is True:
        password = "".join(sample((l+m), number))
        password = password.lower()
        return password
    
    if condition1 is True and condition2 is True:
        password = "".join(sample((n+m), number))
        password = password.lower()
        return password
        

            













    
# if condition1 is True and condition2 is False:
#     password = "".join(sample(n, number))
#     password = password.lower()
#     return password

# if condition1 is False and condition2 is True:
#     password = "".join(sample((l+m), number))
#     password = password.lower()
#     return password

# if condition1 is True and condition2 is True:
#     password = "".join(sample((m+n), number))
#     password = password.lower()
#     return password