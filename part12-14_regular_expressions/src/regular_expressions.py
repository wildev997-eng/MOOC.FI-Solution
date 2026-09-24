import re

def is_dotw(my_string: str):
    found = False
    if re.search("^Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        found = True
    return found

def all_vowels(my_string: str):
    disturb = True
    if re.search("[^aiueo]", my_string):
        disturb = False
    return disturb

def time_of_day(my_string: str):
    check = False
    if re.search("^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string):
        check = True
    return check