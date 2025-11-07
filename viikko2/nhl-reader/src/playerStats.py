from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        nat = nat.upper()
        print("Players from " + nat)
        players = []
        for player_dict in self.reader.get_players():
            player = Player(player_dict)
            if player.nationality == nat:
                players.append(player)
        return sorted(players, key=lambda player: player.goals+player.assists, reverse=True)
