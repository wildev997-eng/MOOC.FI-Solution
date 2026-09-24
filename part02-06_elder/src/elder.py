print("Person 1:")
pep1 = input("Name:")
age1 = int(input("Age:"))
print("Person 2:")
pep2 = input("Name:")
age2 = int(input("Age:"))

if age1 > age2:
    print("The elder is", pep1)
elif age1 < age2:
    print("The elder is", pep2)
else:
    print(pep1, "and", pep2, "are the same age")