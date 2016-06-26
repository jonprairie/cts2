import cts2.application.util.row as row

class tournament(row.row):
    def __init__(
        self,
        name,
        start_julian_date,
        num_player_range
    ):

        #tournament variables
        self.name = name
        self.start_julian_date = start_julian_date
        self.num_player_range = num_player_range
        self.player_list = []

        #state variables
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


    def AddPlayer(self, p):
        if p not in self.player_list:
            self.player_list.append(p)
        self.UpdateRow("players",len(self.player_list))

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

    def IsDoubleRoundRobin(self):
        return False

    def IsInvitational(self):
        return False
