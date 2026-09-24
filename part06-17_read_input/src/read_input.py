def read_input(question: str, bot: int, top: int):
    while True:
        try:
            question =  int(input(f"{question}"))
            if question >= bot and question <= top:
                return question
        
        except ValueError:
            pass

        print(f"You must type in an integer between {bot} and {top}")