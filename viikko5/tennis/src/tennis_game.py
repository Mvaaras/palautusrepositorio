class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.point_names = {
            0:"Love",
            1:"Fifteen",
            2:"Thirty",
            3:"Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = self.define_gamestate()

        return score

    def define_gamestate(self):
        if self.player1_score == self.player2_score:
            return self.name_draw()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.name_lategame()
        else:
            return self.name_earlygame()

    def name_draw(self):
        if self.player1_score < 4:
            return self.name_points(self.player1_score) + "-All"
        return "Deuce"

    def name_lategame(self):
        point_difference = self.player1_score - self. player2_score
        if point_difference > 0:
            return self.build_lategame_name("1",point_difference)
        return self.build_lategame_name("2",abs(point_difference))

    def name_earlygame(self):
        return self.point_names[self.player1_score] + "-" + self.point_names[self.player2_score]

    def build_lategame_name(self, player, point_difference):
        if point_difference == 1:
            return "Advantage player" + player
        return "Win for player" + player

    def name_points(self,points):
        return self.point_names[points]
