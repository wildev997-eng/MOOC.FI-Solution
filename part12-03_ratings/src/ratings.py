def sort_by_ratings(items: list):

    def sort_movie(items: list):
        return [items[rating] for rating in items if rating == "rating" ]
    
    return sorted(items, key=sort_movie, reverse=True)