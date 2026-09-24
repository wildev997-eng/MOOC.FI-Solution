class HockeyApp:
    def __init__(self):
        self.file_name = None
        self.players = []
    
    def browse_json(self):
        import json
        
        file_name = input("file name:")
        self.file_name = file_name
        with open(file_name) as reading:
            data = reading.read()

        self.players = json.loads(data)
        
        print(f"read the data of {len(self.players)} players")
    
    def search(self):
        name = input("name: ")
        matches = [index for index in self.players if index["name"] == name]
        
        if not matches:
            print("no matches")
            return
        
        for player in matches:
            points = player["goals"] + player["assists"]
            print(f"{player['name']:<21}{player['team']:<3}{player['goals']:>4} + {player['assists']:>2} = {points:>3}")

    def team(self):
        team = [index["team"] for index in self.players]
        unique = set(team)
        sorting = sorted(unique)
        return [print(index) for index in sorting]
    
    def countries(self):
        countries = [index["nationality"] for index in self.players]
        unique = set(countries)
        sorting = sorted(unique)
        return [print(index) for index in sorting]
    
    def player_in_team(self):
        team = input("team:")
        matches = [index for index in self.players if index["team"] == team]

        if not matches:
            print("no matches")
            return
        
        matches = sorted(matches, key=lambda player: player["goals"] + player["assists"], reverse=True)

        for player in matches:
            points = player["goals"] + player["assists"]
            print(f"{player['name']:<21}{player['team']:<3}{player['goals']:>4} + {player['assists']:>2} = {points:>3}")

    def player_in_country(self):
        country = input("country:")
        matches = [index for index in self.players if index["nationality"] == country]

        if not matches:
            print("no matches")
            return

        matches = sorted(matches, key=lambda player: player["goals"] + player["assists"], reverse=True)

        for player in matches:
            points = player["goals"] + player["assists"]
            print(f"{player['name']:<21}{player['team']:<3}{player['goals']:>4} + {player['assists']:>2} = {points:>3}")

    def most_points(self):
        count = int(input("how many:"))
        listing = sorted(
            self.players,
            key=lambda player: (player["goals"] + player["assists"], player["goals"]),
            reverse=True
        )
        
        amount = listing[:count]

        for player in amount:
            points = player["goals"] + player["assists"]
            print(f"{player['name']:<21}{player['team']:<3}{player['goals']:>4} + {player['assists']:>2} = {points:>3}")
    
    def most_goals(self):
        count = int(input("how many:"))
        listing = sorted(
            self.players,
            key=lambda player: (player["goals"], -player["games"]),
            reverse=True
        )
        
        amount = listing[:count]

        for player in amount:
            points = player["goals"] + player["assists"]
            print(f"{player['name']:<21}{player['team']:<3}{player['goals']:>4} + {player['assists']:>2} = {points:>3}")
    

    def helps(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        self.browse_json()
        print()
        self.helps()
        while True:
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.search()
            elif command == "2":
                self.team()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.player_in_team()
            elif command == "5":
                self.player_in_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.commands()


application = HockeyApp()
application.execute()