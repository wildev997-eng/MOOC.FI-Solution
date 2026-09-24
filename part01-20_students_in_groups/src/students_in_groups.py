x = int(input("How many students on the course?"))
y = int(input("Desired group size?"))
print(f"Number of groups formed: {(x+y-1)//y}")