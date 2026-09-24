def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

numbers = prime_numbers()
for i in range(8):
    print(next(numbers))