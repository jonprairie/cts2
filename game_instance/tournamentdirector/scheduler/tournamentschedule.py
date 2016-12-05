class tournamentschedule:
    def __init__(self, num_rounds=0):
        self.started  = False
        self.finished = False
        self.player_list = []
        self.rounds = []
        self.num_rounds = num_rounds
        self.current_round_index = 0

    def Start(self, player_list):
        self.player_list = player_list
        self.started = True

    def BuildRoundSchedule(self):
        pass

    def SetNumRounds(self, rounds):
        pass

    def SimulateCurrentRound(self):
        for game in self.GetCurrentRound().GetGames():
            game.Simulate()
        self.current_round_index += 1
        if self.current_round_index >= self.num_rounds:
            self.finished = True

    def IsStarted(self):
        return self.started

    def IsFinished(self):
        return self.finished

    def IsCurrent(self):
        return self.IsStarted() and not self.IsFinished()

    def GetCurrentRound(self):
        return self.rounds[self.current_round_index]

    def GetSchedule(self):
        return self

    def GetRounds(self):
        return self.rounds

    def GetNumRounds(self):
        pass

    def GetMaxNumberRounds(self, max_players):
        pass
