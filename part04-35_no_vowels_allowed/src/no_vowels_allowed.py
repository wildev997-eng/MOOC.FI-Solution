def no_vowels(x: str):
    vowel = ["a", "i", "u", "e", "o"]
    for grab in vowel:
        x = x.replace(grab, "")

    return x