class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.team = player_data['team']
        self.games = player_data['games']
        self.id = player_data['id']

    def get_score(self):
        return self.goals + self.assists

    def __str__(self):
        text = f"""{self.name:20} Teams:{self.team:15} G:{self.goals} + A:{self.assists} = {self.get_score()}"""
        return text
