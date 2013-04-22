class WarELO:

    def __init__(self, ELO1, ELO2, brute_force=0, prev_wars=0):
        """
        ELO1, ELO2: player1, player2 ratings
        brute_force: rating modifier based on kingdoms relative brute force for player1 (-400...+400)
        prev_wars: number of wars players have had previously
        """
        self.ELO1 = ELO1
        self.ELO2 = ELO2
        self.brute_force = brute_force
        self.prev_wars = prev_wars


    def ELO_change(self, result=0.5, k=32):
        """
        Standard ELO change
        """
        return k * (result - 1.0 / ( 1.0 + 10**((self.ELO2-self.ELO1-self.brute_force)/400.0)))

    def change(self, result=0.5, activity=1.0, k=32):
        """
        returns ELO change for player1 (to add) and player2 (to substract)
        when normal player played against player with provisional rating then his rating should remain unchanged
        result: 0-loss for player1, 0.5-draw, 1.0-win for player1
        activity: player activity rating
        k: max rating change constant
        """
        if self.prev_wars < 2:
            prev_wars_factor = 1.0
        else:
            prev_wars_factor = 0.5 ** (self.prev_wars - 1)
        return round(self.ELO_change(result, k) * activity * prev_wars_factor)

