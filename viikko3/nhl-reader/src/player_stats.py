class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def check_nationality(self, player, nation):
        if player.nationality == nation:
            return True
        return False
    
    def points(self, player):
        return player.points()

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = []
        for player in self.reader.read:
            if self.check_nationality(player, nationality):
                players_of_nationality.append(player)
        return sorted(players_of_nationality, key=self.points, reverse=True)