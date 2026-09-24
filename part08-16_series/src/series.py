class Series:
    def __init__(self,title:str, season:int, genre:list):
        self.title = title
        self.season = season
        self.genre = genre
        self.rate_count = 0
        self.total = 0
    
    def rate(self, rating:int):
        self.rate_count += 1
        self.total += rating
        self.rating = self.total / self.rate_count


    def __str__(self):
        if self.rate_count == 0:
            return f"{self.title} ({self.season} seasons)\n" f"genres: {", ".join(self.genre)}\n" f"no ratings"
        else:
            return f"{self.title} ({self.season} seasons)\n" f"genres: {", ".join(self.genre)}\n" f"{self.rate_count} ratings, average {self.rating:.1f} points"

def minimum_grade(rating: float, series_list: list):
    catch = []
    for index in series_list:
        if index.rating >= rating:
            catch.append(index)
    
    return catch

def includes_genre(genre: str, series_list: list):
    catching = []
    for index in series_list:
        if genre in index.genre:
            catching.append(index)

    return catching
