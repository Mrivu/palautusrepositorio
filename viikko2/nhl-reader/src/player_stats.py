from rich.table import Table
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.make_table()

    def make_table(self):
        self.table = Table(title="NHL Players")
        self.table.add_column("Player name", justify="left", style="cyan", no_wrap=True)
        self.table.add_column("Player teams", justify="left", style="magenta")
        self.table.add_column("Goals", justify="right", style="green")
        self.table.add_column("Assists", justify="right", style="green")
        self.table.add_column("Points", justify="right", style="green")

    def top_scorers_by_nationality(self, nat):
        self.make_table()
        nat = nat.upper()
        print("Players from " + nat)
        players = self.reader.get_players()

        for player_dict in sorted(players, key=lambda player: player["goals"]+player["assists"], reverse=True):
            player = Player(player_dict)
            if player.nationality == nat:
                self.table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.get_score()))
        return self.table
