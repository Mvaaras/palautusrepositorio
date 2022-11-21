import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.read = []
        response = requests.get(url).json()
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['penalties'],
                player_dict['games'],
                player_dict['nationality']
            )
            self.read.append(player)

    def get_players(self):
        return self.read
