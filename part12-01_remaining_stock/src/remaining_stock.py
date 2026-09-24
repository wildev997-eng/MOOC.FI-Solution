def sort_by_remaining_stock(items: list):

    def sort_order(item: tuple):
        return item [2]

    return sorted(items, key=sort_order)
