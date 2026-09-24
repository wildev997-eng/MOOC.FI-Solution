class Task:
    iden = 0

    def __init__(self, description: str, programmer, workload: int):
        Task.iden += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.iden
        self.status = False

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"NOT FINISHED" if self.status == False else "FINISHED"}"
    

    
    def is_finished(self):
        return self.status
    
    def mark_finished(self):
        self.status = True

class OrderBook:
    def __init__(self):
        self.book_container = []

    def add_order(self, description, programmer, workload):
        new_task = Task(description, programmer, workload)
        self.book_container.append(new_task) 
    
    def all_orders(self):
        return self.book_container
    
    def programmers(self):
        prog =  list(set([index.programmer for index in self.book_container]))
        return prog
    
    def mark_finished(self, id: int):
        avail = False
        for index in self.book_container:
            if index.id == id:
                index.status = True
                avail = True
        if not avail:
            raise ValueError
        
    def finished_orders(self):
        return [index for index in self.book_container if index.status == True]

    def unfinished_orders(self):
        return [index for index in self.book_container if index.status == False]

    def status_of_programmer(self, programmer: str):
        is_dev = False
        for index in self.book_container:
            if index.programmer == programmer:
                is_dev = True
        
        if is_dev:
            finished = len([index for index in self.book_container if index.status == True and index.programmer == programmer])   
            unfinished = len([index for index in self.book_container if index.status == False and index.programmer == programmer])
            finished_sum = sum([index.workload for index in self.book_container if index.status == True and index.programmer == programmer])
            unfinished_sum = sum([index.workload for index in self.book_container if index.status == False and index.programmer == programmer])
            return (finished, unfinished, finished_sum, unfinished_sum)
        else:
            raise ValueError