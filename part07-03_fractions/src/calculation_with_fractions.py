def fractionate(amount: int):
    from fractions import Fraction
    listing = []

    x = Fraction(1, amount)

    for grabing in range(amount):
        listing.append(x)

    return listing