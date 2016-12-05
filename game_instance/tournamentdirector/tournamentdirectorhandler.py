"""
handles processing and maintenance of tournament directors
"""
import cts2.util.pkg as pkg
import tournamentdirector
import recruiter.inviterecruiter as inviterecruiter
import recruiter.openrecruiter as openrecruiter
import scheduler.roundrobinschedule as roundrobinschedule
import scheduler.matchschedule as matchschedule
import random

class tournamentdirectorhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "tournament_director_handler",
            [
                "create_random_tournament_director",
                "get_tournament_director_list"
            ],
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
            [
                "round_robin_player_range",
                "swiss_player_range",
                "match_player_range"
            ]
        )

    def CreateRandomTournamentDirector(self):
        tournament = self.api.Call("create_random_tournament")
        scheduler = self.GetRandomScheduler()
        recruiter = self.GetRandomRecruiter(
            tournament,
            self.default_options[
                scheduler.GetType() + "_player_range"
            ]
        )
        return self.CreateTournamentDirector(
            tournament,
            recruiter,
            scheduler
        )

    def GetRandomRecruiter(self, tournament, player_range):
        if random.randint(0,1):
            return inviterecruiter.inviterecruiter(
                tournament,
                player_range,
                self.api.Call("create_tournament_outbox", tournament),
                lambda: self.api.Call("get_player_list")
            )
        else:
            return openrecruiter.openrecruiter(
                tournament,
                player_range,
                self.api.Call("create_tournament_inbox", tournament)
            )

    def GetRandomScheduler(self):
        if random.randint(0,5):
            return roundrobinschedule.roundrobinschedule()
        else:
            return matchschedule.matchschedule(
                random.randint(4,10)
            )

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


    def GetTournamentDirectorList(self):
        return self.td_list
