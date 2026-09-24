def balanced_brackets(my_string: str):
    removed = "".join([index for index in my_string if index in "()[]"])
    
    if len(removed) == 0:
        return True
    if removed[0] == "(" and removed[-1] != ")" or removed[0] == "[" and removed[-1] != "]" or len(removed) % 2 != 0:
        return False
    
    return balanced_brackets(removed[1:-1])


# ok = balanced_brackets("([([])])")
# print(ok)

# ok = balanced_brackets("(python version [3.7]) please use this one!")
# print(ok)

# # this is no good, the closing bracket doesn't match
# ok = balanced_brackets("(()]")
# print(ok)

# # different types of brackets are mismatched
# ok = balanced_brackets("([bad egg)]")
# print(ok)