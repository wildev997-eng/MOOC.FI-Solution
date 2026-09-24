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
        print(self.book_container)
    
    def programmers(self):
        prog =  list(set([index.programmer for index in self.book_container]))
        print(prog)
    
    def mark_finished(self, id: int):
        avail = False
        for index in self.book_container:
            if index.id == id:
                index.status = True
                avail = True
        if not avail:
            raise ValueError
        
    def finished_orders(self):
        finished = [task for task in self.book_container if task.status == True]
        if not finished:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def unfinished_orders(self):
        unfinished = [task for task in self.book_container if not task.status]
        if not unfinished:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)

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
            print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_sum} scheduled {unfinished_sum}")
        else:
            raise ValueError

class OrderApp:
    def __init__(self):
        self.orderapp = OrderBook()
    
    def commands(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmers")
    
    def add_order(self):
        description = input("description: ")
        progwork = input("programmer and workload estimate: ")
        try:
            spliting = progwork.split(" ")
            programmer = spliting[0]
            workload = int(spliting[1])
            self.orderapp.add_order(description, programmer, workload)
            print("added!")
        except (ValueError, IndexError):
            print("erroneous input")
    
    def finished_task(self):
        self.orderapp.finished_orders()
    
    def unfinished_task(self):
        self.orderapp.unfinished_orders()   
    
    def mark_test(self):
        try:
            id = int(input("id: "))
            self.orderapp.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")
    
    def programmer_list(self):
        self.orderapp.programmers()
    
    def programmer_status(self):
        try:
            programmer = input("programmer: ")
            self.orderapp.status_of_programmer(programmer)
        except ValueError:
            print("erroneous input")

    
    def execute(self):
        self.commands()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.add_order()
            elif command == "2":
                self.finished_task()
            elif command == "3":
                self.unfinished_task()
            elif command == "4":
                self.mark_test()
            elif command == "5":
                self.programmer_list()
            elif command == "6":
                self.programmer_status()
            else:
                self.commands()

application = OrderApp()
application.execute()