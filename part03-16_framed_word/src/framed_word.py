x = input("Word:")
l = int((28 - len(x)) / 2)
r = int((28 - len(x)) - l)
z = l * " "
zz = r * " "

print(30 * "*")

print(f"*{z}{x}{zz}*")

print(30 * "*")
