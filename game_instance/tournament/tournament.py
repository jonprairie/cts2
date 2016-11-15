import cts2.util.row as row
import history.tournamenthistory as th


class tournament(row.row):
    def __init__(
            self,
            name,
            start_julian_date
    ):

        # tournament variables
        self.name = name
        self.player_list = []
        self.start_julian_date = start_julian_date
        self.date_range = []
        self.num_rounds = 0
        self.started = False
        self.finished = False
        self.cancel = False
        # may need to inject history if we end up having multiple
        # tie-breaker definitions etc.
        self.history = None
        # move to history?
        self.champion = None

        row.row.__init__(
            self,
            dict(
                name=self.name,
                players=len(self.player_list),
                start_date=self.start_julian_date
            )
        )

    def __str__(self):
        return self.RowStr()

    def GetChampion(self):
        return self.champion

    def GetSchedule(self):
        return self.schedule

    def RowStr(self):
        return self.name

    def IsCancelled(self):
        return self.cancel

    def IsCurrent(self):
        return self.started and not self.finished

    def IsStarted(self):
        return self.started

    def IsFinished(self):
        return self.finished

    def GetNumPlayers(self):
        return len(self.player_list)

    def GetDateRange(self):
        return self.date_range

    def PlaysToday(self, date):
        return date in self.date_range

    def AddPlayer(self, player):
        if player not in self.player_list:
            self.player_list.append(player)
        self.UpdateRow("players", len(self.player_list))

    def AddPlayerList(self, player_list):
        for player in player_list:
            self.AddPlayer(player)

    def GetStandings(self):
        return self.history.GetStandings()

    def Conflicts(self, other_tourn):
        return set(self.GetDateRange()) & set(other_tourn.GetDateRange())

    def CancelTournament(self):
        self.cancel = True
        for player in self.player_list:
            player.CancelTournament(self)

    def Start(self, player_list, schedule):
        self.started = True
        self.AddPlayerList(player_list)
        self.history = th.tournamenthistory(player_list)
        self.schedule = schedule
        self.date_range = [
            self.start_julian_date+offset
            for offset in range(self.GetSchedule().GetNumRounds())
        ]

    def SetWorstCaseDateRange(self, max_players):
        self.date_range = [
            self.start_julian_date+offset for offset in range(max_players)
        ]

    def Finish(self):
        self.finished = True
