def sort_by_seasons(items: list):
    def movie_sort(items:list):
        for index in items:
            return [items[index] for index in items if index == "seasons"]
    
    return sorted(items, key=movie_sort)



# shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

# for show in sort_by_seasons(shows):
#     print(f"{show['name']} {show['seasons']} seasons")