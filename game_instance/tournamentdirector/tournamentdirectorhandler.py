"""
handles processing and maintenance of tournament directors
"""
import cts2.util.pkg as pkg
import tournamentdirector
import recruiter.inviterecruiter as inviterecruiter
import scheduler.roundrobinschedule as roundrobinschedule
import random

class tournamentdirectorhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "tournament_director_handler",
            ["create_random_tournament_director"],
            [
                "register_for_maintenance",
                "def_options"
            ],
            save_ind=True
        )
        self.td_list = []

    def Activate(self):
        self.api.Call("register_for_maintenance", self, ["daily"])
        self.default_options = self.api.Call(
            "def_options",
            ["round_robin_player_range"]
        )

    def CreateRandomTournamentDirector(self):
        tournament = self.api.Call("create_random_tournament")
        recruiter = self.GetRandomRecruiter(tournament)
        scheduler = self.GetRandomScheduler()
        return self.CreateTournamentDirector(
            tournament,
            recruiter,
            scheduler
        )

    def GetRandomRecruiter(self, tournament):
        return inviterecruiter.inviterecruiter(
            tournament,
            self.default_options["round_robin_player_range"],
            lambda: self.api.Call("get_player_list")
        )

    def GetRandomScheduler(self):
        return roundrobinschedule.roundrobinschedule()

    def CreateTournamentDirector(self, tournament, recruiter, scheduler):
        temp_td = tournamentdirector.tournamentdirector(
            tournament,
            recruiter,
            scheduler
        )
        self.td_list.append(temp_td)
        return temp_td

    def DailyMaintenance(self, dte):
        for td in self.td_list:
            td.Maintenance(dte)

