import cts2.util.row as row


class tournament(row.row):
    def __init__(
        self,
        name,
        start_julian_date,
        num_player_range
    ):

        # tournament variables
        self.name = name
        self.start_julian_date = start_julian_date
        self.num_player_range = num_player_range
        self.player_list = []
        self.date_range = []

        # state variables
        self.started = False
        self.finished = False
        self.cancel = False

        row.row.__init__(
            self,
            dict(
                name=self.name,
                players=len(self.player_list),
                start_date=start_julian_date
            )
        )

    def __str__(self):
        return self.RowStr()

    def RowStr(self):
        return "tournament." + self.name

    def IsFinished(self):
        return self.finished

    def AddPlayer(self, p):
        if p not in self.player_list:
            self.player_list.append(p)
        self.UpdateRow("players", len(self.player_list))

    def SetDateRange(self, date_range):
        self.date_range = date_range

    def GetDateRange(self):
        return self.date_range

    def Conflicts(self, t):
        if (set(self.GetDateRange()) & set(t.GetDateRange())):
            return True
        else:
            return False

    def CancelTournament(self):
        self.cancel = True
        for p in self.player_list:
            p.CancelTournament(self)

    def PlayRound(self):
        self.current_round.Simulate()
        self.current_round_index += 1
        if self.current_round_index == len(self.schedule):
            self.finished = True
        else:
            self.current_round = self.schedule[
                self.current_round_index
            ]

    def HasEnoughPlayers(self):
        return self.num_player_range[0] <= len(self.player_list)

    def IsCurrent(self):
        return self.started and not self.finished and not self.cancel

    def IsDoubleRoundRobin(self):
        return False

    def IsInvitational(self):
        return False
