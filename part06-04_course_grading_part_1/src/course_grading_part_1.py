si = input("Student information:")
ec = input("Exercises completed:")

def student_information():
    with open(si) as reading:
        si_container = {}
        for content in reading:
            begone = content.replace("\n", "")
            parts = begone.split(";")
            if parts[0] == "id":
                continue
            si_container[parts[0]] = [" ".join(parts[1:])]
        return si_container

def exercise_completed():
    with open(ec) as reading:
        ec_container = {}
        for content in reading:
            begone = content.replace("\n", "")
            parts = begone.split(";")
            if parts[0] == "id":
                continue
            ec_container[parts[0]] = parts[1:]
        return ec_container

call_si = student_information()
call_ec = exercise_completed()

for printing_si in call_si:
    for printing_ec in call_ec:
        for index in call_si[printing_si]:
            summ = 0
            for element in call_ec[printing_ec]:
                summ += int(element)
            if printing_si == printing_ec:
                print(f"{index} {summ}")