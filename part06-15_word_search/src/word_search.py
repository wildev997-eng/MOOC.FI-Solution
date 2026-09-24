def find_words(search_term: str):
    search_term = search_term.lower()
    if "." in search_term:
        with open("words.txt") as content:
            wordle = []
            matching_dot = []
            for index in content:
                strips = index.strip()
                wordle.append(strips)

            for index in wordle:
                if len(index) == len(search_term):
                    bingo = True
                    for n in range(len(search_term)):
                        if search_term[n] != "." and search_term[n] != index[n]:
                            bingo = False
                    if bingo:
                        matching_dot.append(index)                 
        return matching_dot
    
    elif "*" in search_term:
        with open("words.txt") as content:
            wordling = []
            matching_asterik = []
            for index in content:
                strips = index.strip()
                wordling.append(strips)
            
            if search_term[-1] == "*":
                x = search_term[0:-1]
                l = len(search_term) - 1
                for index in wordling:
                    if index[:l] == x:
                        matching_asterik.append(index)
            
            if search_term[0] == "*":
                y = search_term[1:]
                ll = (len(search_term)-1) * -1
                for index in wordling:
                    if index[ll:] == y:
                        matching_asterik.append(index)
        return matching_asterik
    
    else:
        with open("words.txt") as content:
            wordlist = []
            matching_complete = []
            for index in content:
                strips = index.strip()
                wordlist.append(strips)
        
            for index in wordlist:
                if index == search_term:
                    matching_complete.append(index)
        return matching_complete
            