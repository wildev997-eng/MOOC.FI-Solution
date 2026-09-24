def new_person(name: str, age: int):
    if age > 150 or len(name.split(" ")) < 2 or name == "" or len(name) > 40 or age < 0:
        raise ValueError("data invalid")
    else:
        return (name,age)