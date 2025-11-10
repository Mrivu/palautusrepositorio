from rich.console import Console
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    console = Console()
    console.print(players)

if __name__ == "__main__":
    main()
