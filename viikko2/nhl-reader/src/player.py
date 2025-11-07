class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']

    
    def __str__(self):
        text = f"""{self.name}, Nat:{self.nationality} A:{self.assists} G:{self.goals} Team:{self.team} Games:{self.games} Id:{self.id}"""
        return text

