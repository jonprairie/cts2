import cts2.application.util.pkg as pkg
import cts2.application.util.stringtable as stringtable
import cts2.database.tournamentnameinterface as tournamentnameinterface
import cts2.game_instance.tournament.drrinvitational as drrinvitational
import random


class tournamenthandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "tournament_handler",
            [
                "create_tournament",
                "create_random_tournament",
                "get_current_tournament_list",
                "get_non_started_tournament_list"
            ],
            ["register_for_maintenance"]
        )
        self.tournament_list = []

    def Activate(self):
        self.api.Call("register_for_maintenance", ["daily"])

    def CreateTournament(self):
        return self.CreateRandomTournament()

    def CreateRandomTournament(self):
        start_date = random.randint(15, 365)
        name = tournamentnameinterface.GenRandTournamentName()
        new_tournament = drrinvitational.drrinvitational(
            name,
            start_date,
            self.default_options["round_robin_player_range"]
        )
        self.tournament_list.append(new_tournament)
        return new_tournament

    def GetCurrentTournaments(self):
        return self.tournament_list

    def GetFutureTournaments(self, ev):
        return self.tournament_list

    def SendInvites(self, t):
        random.shuffle(
            self.player_list
        )
        for p in self.get_player_list.player_list:
            if t.SendInvite(p):
                pass
            if t.InvitesFull():
                break

    def DailyMaintenance(self, date):
        self.get_player_list = self.api.Call("get_player_list")
        for t in self.tournament_list:
            if not t.finished and not t.started and t.sends_invites:
                self.SendInvites(t)
            if int(t.start_julian_date) == int(date):
                if t.HasEnoughPlayers():
                    t.started = True
                else:
                    t.CancelTournament()
            if t.started and not t.schedule_finished:
                t.BuildSchedule()
            if t.started and not t.finished:
                t.PlayRound()
            if not t.started and not t.cancel and (
                int(date) > int(t.start_julian_date)
            ):
                self.api.Call(
                    "log_msg",
                    str(t) + " error, start date is " +
                    str(t.start_julian_date) +
                    " today is " + str(date)
                )
