class Checklist:
    def __init__(self, head:str, entries:list):
        Checklist.header = head
        Checklist.entries = entries

class Customer:
    def __init__(self, id:str, balance:float, discount:int):
        Customer.id = id
        Customer.balance = balance
        Customer.discount = discount

class Cable:
    def __init__(self, model:str, length:float, max_speed:int, bidirectional:bool):
        Cable.model = model
        Cable.length = length
        Cable.max_speed = max_speed
        Cable.bidirectional = bidirectional