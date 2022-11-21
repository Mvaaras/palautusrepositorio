class Player:
    def __init__(self, name, team, goals, assists, penalties, games, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        self.games = games
        self.nationality = nationality

    def points(self):
        return self.games + self.assists

    def __str__(self):
        return (f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.points():3}")