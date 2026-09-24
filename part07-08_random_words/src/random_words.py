def words(n: int, beginning: str):
    from random import shuffle

    with open("words.txt") as content:
        wordlist = []
        for index in content:
            strips = index.strip()
            wordlist.append(strips)

        shuffle(wordlist)

        l = len(beginning)
        shuffling = []
        for index in wordlist:
            if index[:l] == beginning:
                shuffling.append(index)
        
        if len(shuffling) < n:
            raise ValueError
        else:
            return shuffling[:n]
