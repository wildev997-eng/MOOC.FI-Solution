# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
        self.total = 0

    def add_number(self, number:int):
        self.numbers += number
        self.counter += 1
        self.total += number

    def count_numbers(self):
        return self.counter
    
    def get_sum(self):
        return self.total

    def average(self):
        if self.counter == 0:
            return False
        else:
            mean = self.total / self.counter
            return mean

        


print("Please type in integer numbers:")
stats = NumberStats()
even = NumberStats()
odds = NumberStats()
while True:
    x = int(input(""))

    if x == -1:
        break

    if x % 2 == 0:
        even.add_number(x)
    else:
        odds.add_number(x)

    stats.add_number(x)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odds.get_sum()}")