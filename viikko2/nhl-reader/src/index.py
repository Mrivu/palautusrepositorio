import requests
from player import Player

def main():
    get_by_nationality("FIN")

def get_data():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    return requests.get(url).json()

def get_by_nationality(nat):
    nat = nat.upper()
    print("Players from " + nat)
    players = []
    for player_dict in get_data():
        player = Player(player_dict)
        if player.nationality == nat:
            players.append(player)
    for player in sorted(players, key=lambda player: player.goals+player.assists, reverse=True):
        print(player)

if __name__ == "__main__":
    main()