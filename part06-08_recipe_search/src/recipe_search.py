def search_by_name(filename: str, word: str):
    with open(filename) as reading :
        recipe_dict = {}
        container = []
        current = []
        for index in reading:
            index = index.strip()
            container.append(index)
        for index in container:
            if index == "":
                name = current[0]
                time = current[1]
                ingredients = current[2:]
                recipe_dict[name] = [time] + ingredients
                current = []
            else:
                current.append(index)
        recipe_dict[current[0]] = current[1:]
    
    #finding the recipe:
    searching = []
    for index in recipe_dict:
        if word in index.lower():
            searching.append(index)
    return searching

def search_by_time(filename: str, prep_time: int):
    with open(filename) as reading :
        recipe_dict = {}
        container = []
        current = []
        for index in reading:
            index = index.strip()
            container.append(index)
        for index in container:
            if index == "":
                name = current[0]
                time = current[1]
                ingredients = current[2:]
                recipe_dict[name] = [time] + [ingredients]
                current = []
            else:
                current.append(index)
        name = current[0]
        time = current[1]
        ingredients = current[2:]
        recipe_dict[name] = [time] + [ingredients]
    x = 0
    prep = []
    for index, time in recipe_dict.items():
        if prep_time >= int(time[x]) and int(time[x]) < prep_time:
            prep.append(f"{index}, preparation time {time[x]} min")
    return prep

def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as reading :
        recipe_dict = {}
        container = []
        current = []
        for index in reading:
            index = index.strip()
            container.append(index)
        for index in container:
            if index == "":
                name = current[0]
                time = current[1]
                ingredients = current[2:]
                recipe_dict[name] = [time] + [ingredients]
                current = []
            else:
                current.append(index)
        name = current[0]
        time = current[1]
        ingredients = current[2:]
        recipe_dict[name] = [time] + [ingredients]
    
    ingred = []
    for index, time in recipe_dict.items():
        for element in time:
            if ingredient in element:
                ingred.append(f"{index}, preparation time {time[0]} min")
            
    return ingred




if __name__ == "__main__":
    # found_recipes = search_by_name("recipes1.txt", "cake")
    # for recipe in found_recipes:
    #     print(recipe)
    # found_recipes = search_by_time("recipes1.txt", 20)
    # for recipe in found_recipes:
    #     print(recipe)
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)