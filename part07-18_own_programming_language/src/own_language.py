def run(program: list):
    import string

    location = {}
    sequence = {}
    res = []
    line_number = 0

    for i, content in enumerate(program):
        if content.endswith(":"):
            location[content[:-1]] = i

    while line_number < len(program):
        content = program[line_number]
        spliting = content.split(" ")

        try:
            if spliting[0] == "MOV" and int(spliting[2]) - int(spliting[2]) == 0 :
                sequence[spliting[1]] = spliting[2]
        except ValueError:
            sequence[spliting[1]] = sequence[spliting[2]]

        try:
            if spliting[0] == "PRINT" and spliting[1] in string.ascii_uppercase:
                res.append(int(sequence[spliting[1]]))
            elif spliting[0] == "PRINT" and int(spliting[1]) - int(spliting[1]) == 0:
                res.append(int(spliting[1]))
        except KeyError:
            res.append(0)
        
        try:
            if spliting[0] == "ADD":
                sequence[spliting[1]] = int(sequence[spliting[1]]) + int(spliting[2])
            elif spliting[0] == "SUB":
                sequence[spliting[1]] = int(sequence[spliting[1]]) - int(spliting[2])
        except (TypeError, ValueError):
            if spliting[0] == "ADD":
                sequence[spliting[1]] = int(sequence[spliting[1]]) + int(sequence[spliting[2]])
            elif spliting[0] == "SUB":
                sequence[spliting[1]] = int(sequence[spliting[1]]) - int(sequence[spliting[2]])
        except KeyError:
            if spliting[1] not in sequence:
                sequence[spliting[1]] = spliting[2]
        
        try:
            if spliting[0] == "MUL" and int(spliting[2]) - int(spliting[2]) == 0:
                sequence[spliting[1]] = int(sequence[spliting[1]]) * int(spliting[2])
        except ValueError:
            sequence[spliting[1]] = int(sequence[spliting[1]]) * int(sequence[spliting[2]])
        
        if spliting[0] == "END":
            return res
            break

        if spliting[0] == "IF":

            try:
                if spliting[2] == "<" and int(spliting[3]) - int(spliting[3]) == 0 and int(sequence[spliting[1]]) < int(spliting[3]):
                    line_number = int(location[spliting[5]])
                    continue
            except ValueError:
                if spliting[2] == "<" and spliting[3] in string.ascii_uppercase and int(sequence[spliting[1]]) < int(sequence[spliting[3]]):
                    line_number = int(location[spliting[5]])
                    continue

            try:
                if spliting[2] == ">" and int(spliting[3]) - int(spliting[3]) == 0 and int(sequence[spliting[1]]) > int(spliting[3]):
                    line_number = int(location[spliting[5]])
                    continue
            except ValueError:
                if spliting[2] == ">" and spliting[3] in string.ascii_uppercase and int(sequence[spliting[1]]) > int(sequence[spliting[3]]):
                    line_number = int(location[spliting[5]])
                    continue
            
            try:
                if spliting[2] == "<=" and int(spliting[3]) - int(spliting[3]) == 0 and int(sequence[spliting[1]]) <= int(spliting[3]):
                    line_number = int(location[spliting[5]])
                    continue
            except ValueError:
                if spliting[2] == "<=" and spliting[3] in string.ascii_uppercase and int(sequence[spliting[1]]) <= int(sequence[spliting[3]]):
                    line_number = int(location[spliting[5]])
                    continue

            try:
                if spliting[2] == ">=" and int(spliting[3]) - int(spliting[3]) == 0 and int(sequence[spliting[1]]) >= int(spliting[3]):
                    line_number = int(location[spliting[5]])
                    continue
            except ValueError:
                if spliting[2] == ">=" and spliting[3] in string.ascii_uppercase and int(sequence[spliting[1]]) >= int(sequence[spliting[3]]):
                    line_number = int(location[spliting[5]])
                    continue

            try:
                if spliting[2] == "==" and int(spliting[3]) - int(spliting[3]) == 0 and int(sequence[spliting[1]]) == int(spliting[3]):
                    line_number = int(location[spliting[5]])
                    continue
            except ValueError:
                if spliting[2] == "==" and spliting[3] in string.ascii_uppercase and int(sequence[spliting[1]]) == int(sequence[spliting[3]]):
                    line_number = int(location[spliting[5]])
                    continue

            try:
                if spliting[2] == "!=" and int(spliting[3]) - int(spliting[3]) == 0 and int(sequence[spliting[1]]) != int(spliting[3]):
                    line_number = int(location[spliting[5]])
                    continue
            except ValueError:
                if spliting[2] == "!=" and spliting[3] in string.ascii_uppercase and int(sequence[spliting[1]]) != int(sequence[spliting[3]]):
                    line_number = int(location[spliting[5]])
                    continue
        
        if spliting[0] == "JUMP":
            line_number = int(location[spliting[1]])
            

        line_number += 1

    return res






if __name__ == "__main__":
    program4 = ['MOV A 1', 'MOV B 999', 'start:', 'ADD A 1', 'SUB B 1', 'ADD C 1', 'IF A == B JUMP end', 'JUMP start', 'end:', 'PRINT C']
    # program4.append("MOV N 50")
    # program4.append("PRINT 2")
    # program4.append("MOV A 3")
    # program4.append("begin:")
    # program4.append("MOV B 2")
    # program4.append("MOV Z 0")
    # program4.append("test:")
    # program4.append("MOV C B")
    # program4.append("new:")
    # program4.append("IF C == A JUMP error")
    # program4.append("IF C > A JUMP over")
    # program4.append("ADD C B")
    # program4.append("JUMP new")
    # program4.append("error:")
    # program4.append("MOV Z 1")
    # program4.append("JUMP over2")
    # program4.append("over:")
    # program4.append("ADD B 1")
    # program4.append("IF B < A JUMP test")
    # program4.append("over2:")
    # program4.append("IF Z == 1 JUMP over3")
    # program4.append("PRINT A")
    # program4.append("over3:")
    # program4.append("ADD A 1")
    # program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)


#ver 1.0
        # try:
        #     if spliting[0] == "MOV":
        #         sequence[number[spliting[1]]] = spliting[2]
        # except IndexError:
        #     sequence.append(spliting[2])
        
        # try:
        #     if spliting[0] == "ADD":
        #         sequence[number[spliting[1]]] = int(sequence[number[spliting[1]]]) + int(spliting[2])
        #     elif spliting[0] == "SUB":
        #         sequence[number[spliting[1]]] = int(sequence[number[spliting[1]]]) - int(spliting[2])
        #     elif spliting[0] == "MUL":
        #         sequence[number[spliting[1]]] = int(sequence[number[spliting[1]]]) * int(spliting[2])
        # except ValueError:
        #     if spliting[0] == "ADD":
        #         sequence[number[spliting[1]]] = int(sequence[number[spliting[1]]]) + int(sequence[number[spliting[2]]])
        #     elif spliting[0] == "SUB":
        #         sequence[number[spliting[1]]] = int(sequence[number[spliting[1]]]) - int(sequence[number[spliting[2]]])
        #     elif spliting[0] == "MUL":
        #         sequence[number[spliting[1]]] = int(sequence[number[spliting[1]]]) * int(sequence[number[spliting[2]]])
        
        # try:
        #     if spliting[0] == "PRINT":
        #         res.append(int(sequence[number[spliting[1]]]))
        # except IndexError:
        #     res.append(0)
        
        # if spliting[0] == "IF":
        #     if sequence[number[spliting[2]]] == "<":

        #     elif sequence[number[spliting[2]]] == ">":
        #         pass
        #     elif sequence[number[spliting[2]]] == "=<":
        #         pass
        #     elif sequence[number[spliting[2]]] == ">=":
        #         pass
        #     elif sequence[number[spliting[2]]] == "==":
        #         pass
        #     elif sequence[number[spliting[2]]] == "!=":
        #         pass

    #     if spliting[0] == "END":
    #         break
    
    # return res


        
    # print(sequence)
    # print(res)

#ver 1.5
    # for content in program:
    #     spliting = content.split(" ")
    #     try:
    #         if spliting[0] == "MOV" and int(spliting[2]) - int(spliting[2]) == 0 :
    #             sequence[spliting[1]] = spliting[2]
    #     except ValueError:
    #         sequence[spliting[1]] = sequence[spliting[2]]

    #     try:
    #         if spliting[0] == "PRINT":
    #             res.append(int(sequence[spliting[1]]))
    #     except KeyError:
    #         res.append(0)
        
    #     try:
    #         if spliting[0] == "ADD":
    #             sequence[spliting[1]] = int(sequence[spliting[1]]) + int(spliting[2])
    #         elif spliting[0] == "SUB":
    #             sequence[spliting[1]] = int(sequence[spliting[1]]) - int(spliting[2])
    #     except (TypeError, ValueError):
    #         if spliting[0] == "ADD":
    #             sequence[spliting[1]] = int(sequence[spliting[1]]) + int(sequence[spliting[2]])
    #         elif spliting[0] == "SUB":
    #             sequence[spliting[1]] = int(sequence[spliting[1]]) - int(sequence[spliting[2]])
        
    #     try:
    #         if spliting[0] == "MUL" and int(spliting[2]) - int(spliting[2]) == 0:
    #             sequence[spliting[1]] = int(sequence[spliting[1]]) * int(spliting[2])
    #     except ValueError:
    #         sequence[spliting[1]] = int(sequence[spliting[1]]) * int(sequence[spliting[2]])
        
    #     if spliting[0] == "END":
    #         break

    #     if spliting[0].islower():
    #         res.append(spliting[0])
    
    # return res