def word_generator(characters: str, length: int, amount: int):
    import random
    listing = list(characters)
    random.shuffle(listing)
    randomized_string = "".join(listing)
    gen = (randomized_string [i:i+length] for i in range(amount))
    return gen