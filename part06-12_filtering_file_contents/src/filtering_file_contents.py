def filter_solutions():
    student = []
    with open("solutions.csv") as reading:
        for index in reading:
            index = index.strip()
            splitt = index.split(";")
            student.append(splitt)
    
    with open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for index in student:
            sumin = eval(index[1])
            stringer = str(sumin)
            line = ""
            for content in index:
                line += f"{content};"
            line = line[:-1]
            if index[2] == stringer:
                correct_file.write(line + "\n")
            else:
                incorrect_file.write(line + "\n")


filter_solutions()

    # for index in summary:
    #     sumin = eval(index[1])
    #     stringer = str(sumin)
    #     if index[2] == stringer:
    #         with open("correct.csv", "a") as reading:
    #             line = ""
    #             for content in index:
    #                 line += f"{content};"
    #             line = line[:-1]
    #             reading.write(line+"\n")
                
    #     if index[2] != stringer:
    #         with open("incorrect.csv", "a") as reading:
    #             line = ""
    #             for content in index:
    #                 line += f"{content};"
    #             line = line[:-1]
    #             reading.write(line+"\n")