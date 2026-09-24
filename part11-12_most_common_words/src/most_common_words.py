def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        content = f.read().strip().replace("\n", " ").replace(".", "").replace(",", "").split(" ")
        return {word:content.count(word) for word in content if content.count(word) >= lower_limit}