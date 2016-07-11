import cts2.application.util.stringtable as stringtable


class playerhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "player_handler",
            ["get_player_list"],
            [
                "register_for_maintenance",
                "gen_player_list",
                "def_options"
            ]
        )

    def Activate(self):
        self.default_options = self.api.Call(
            "def_options",
            ["num_initial_cpu_players"]
        )
        self.player_list = self.InitPlayers()
        self.api.Call("register_for_maintenance", ["daily"])

    def InitPlayers(self):
        return self.api.Call(
            "gen_player_list",
            self.default_options["num_initial_cpu_players"]
        )

    def GetNumPlayers(self):
        return self.num_players

    def GetPlayerList(self):
        return self.GetPlayers()

    #Get Functions
    def GetPlayers(self):
        return self.player_list

    #Maintenance Functions
    #def RegisterForTournaments(self):
    #    tournament_list = self.tournament_handler.GetNewTournaments()
    #    for p in self.player_list:
    #        p.RegisterForTournaments(tournament_list)

    def DailyMaintenance(self, date):
        # self.RegisterForTournaments()
        for p in self.player_list:
            p.ProcessInvites()

def PlayerCMP(player_x, player_y):
    """returns -1 if player_x's elo is greater than player_y's elo, 0 if they are equal, and 1 otherwise"""

    if player_x.GetElo() > player_y.GetElo():
        return -1
    elif player_y.GetElo() > player_x.GetElo():
        return 1
    else:
        return 0
