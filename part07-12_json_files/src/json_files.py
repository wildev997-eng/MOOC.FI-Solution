def print_persons(filename: str):
    import json

    with open(filename) as reading:
        data = reading.read()

    profile = json.loads(data)

    for index in profile:
        print(f"{index["name"]} {index["age"]} years ({str(index['hobbies']).replace("'", '').replace("[", '').replace("]", '')})")

x = print_persons("file4.json")
print(x)