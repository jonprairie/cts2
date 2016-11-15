"""
handles processing and maintenance of the list of tournaments
"""
import cts2.util.pkg as pkg
import cts2.database.tournamentnameinterface as tournamentnameinterface
import tournament
# import cts2.game_instance.tournament.drrinvitational as drrinvitational
# import cts2.game_instance.tournament.matchinvitational as matchinvitational
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
                "get_current_tournaments",
                "get_future_tournaments",
                "get_tournament_list",
                "get_finished_tournaments"
            ],
            [
                "register_for_maintenance",
                "def_options"
            ],
            save_ind=True
        )
        self.tournament_list = []
        self.default_options = None

    def Activate(self):
        self.api.Call(
            "register_for_maintenance",
            self,
            ["weekly"]
        )
        self.default_options = self.api.Call(
            "def_options",
            [
                "round_robin_player_range",
                "tournament_rate",
                "tourn_buff_lookahead",
                "tourn_buff_range"
            ]
        )

    def CreateTournament(
        self, start_date, type="drr", offset=True,
        country=None
    ):
        if offset:
            start_date += self.api.Call("get_current_julian")
        name = self.CreateTournamentName(country=country)
        new_tournament = None
        if type == "drr":
            name += " drr"
            new_tournament = tournament.tournament(
                name,
                start_date,
            )
        if new_tournament is not None:
            self.tournament_list.append(new_tournament)
        return new_tournament

    def CreateTournamentName(self, country=None):
        ctry_vs_city = 1
        if country is not None:
            if random.randint(0, 10) < 2:
                ctry_vs_city = 0
        if ctry_vs_city == 1:
            noun = self.api.Call("get_random_city", country=country)
        else:
            noun = country
        modifiers = ["chess", "", ""]
        suffixes = [
            "classic", "grand prix", "championship",
            "tournament", "shoot out", "double round robin",
            "match", "invitational", "knockout", "challenge",
            "open", "closed"
        ]
        return (
            str(noun) + " " + random.choice(modifiers) +
            " " + random.choice(suffixes)
        )

    def CreateRandomTournament(self):
        start_date = random.randint(15, 365)
        return self.CreateTournament(start_date, offset=False)

    def GetCurrentTournaments(self):
        return filter(
            lambda t: t.started and not t.finished,
            self.tournament_list
        )

    def GetFinishedTournaments(self):
        return filter(
            lambda t: t.finished,
            self.tournament_list
        )

    def GetTournamentsInRange(self, start=0, length=1):
        today = self.api.Call("get_current_julian")
        temp_list = filter(
            lambda t: t.start_julian_date in range(
                today + start,
                today + start + length
            ),
            self.tournament_list
        )
        self.api.Call(
            "log_msg",
            "today: " + str(today) + "\n" +
            "tournaments found: " + str(len(temp_list)) + "\n" +
            "tournaments: " + "\n".join([
                t.name + ": " + str(
                    t.start_julian_date
                ) for t in self.tournament_list
            ])
        )
        return temp_list

    def GetFutureTournaments(self):
        return filter(
            lambda t: not t.started,
            self.tournament_list
        )

    def GetTournamentList(self):
        return self.tournament_list

    # def SendInvites(self, t, player_list):
    #     random.shuffle(
    #         player_list
    #     )
    #     for p in player_list:
    #         t.SendInvite(p)
    #         if t.InvitesFull():
    #             break

    def BufferTournaments(self):
        """
        buffers tournament pool based on the default option
        tournament_rate (measured in players per current
        tournament).
        """
        upc_t_count = len(self.GetTournamentsInRange(
            start=self.default_options["tourn_buff_lookahead"],
            length=self.default_options["tourn_buff_range"]
        ))
        player_count = len(self.api.Call("get_player_list"))
        exp_count = player_count / self.default_options["tournament_rate"]
        t_diff = exp_count - upc_t_count
        if t_diff > 0:
            num_tournaments = int(abs(random.normalvariate(0, t_diff)))
            start_date_mean = (
                self.default_options["tourn_buff_range"] / 2
            ) + self.default_options["tourn_buff_lookahead"]
            for t in range(num_tournaments):
                start_date = int(random.normalvariate(start_date_mean, 5))
                self.api.Call("create_random_tournament_director")
                # self.CreateTournament(start_date)

    # def TestMatchInvitationals(self):
    #     num_tournaments = int(abs(random.normalvariate(10, 5)))
    #     for t in range(num_tournaments):
    #         start_date = int(random.normalvariate(50, 5))
    #         self.CreateTournament(start_date, type="match")

    def WeeklyMaintenance(self, date):
        self.BufferTournaments()
        # self.TestMatchInvitationals()
