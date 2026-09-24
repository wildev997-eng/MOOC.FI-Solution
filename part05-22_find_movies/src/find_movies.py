def find_movies(database: list, search_term: str):
    search_term.lower()
    grabbing = []
    for index in database:
        if search_term in index["name"].lower():
            grabbing.append(index)
    return grabbing