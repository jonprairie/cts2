"""
handles processing and maintenance of the player list for the
application.
"""
import cts2.util.pkg as pkg
import operator


class playerhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "player_handler",
            [
                "create_random_player",
                "get_player_list",
                "get_top_players_by_elo"
            ],
            ["gen_player"],
            save_ind=True
        )
        self.default_options = dict()
        self.player_list = []

    def CreateRandomPlayer(self):
        temp_player = self.api.Call("gen_player")
        self.player_list.append(temp_player)
        return temp_player

    def InitPlayers(self):
        return self.api.Call(
            "gen_player_list",
            self.default_options["num_initial_cpu_players"]
        )

    def GetPlayerList(self, index_fence=None):
        return self.GetPlayers()

    def GetTopPlayersByElo(self, num_players):
        return sorted(
            self.GetPlayers(),
            key=operator.attrgetter('elo'),
            reverse=True
        )[0:num_players]

    # Get Functions
    def GetPlayers(self):
        return self.player_list

def PlayerCMP(player_x, player_y):
    """returns -1 if player_x's elo is greater than player_y's
    elo, 0 if they are equal, and 1 otherwise"""

    if player_x.GetElo() > player_y.GetElo():
        return -1
    elif player_y.GetElo() > player_x.GetElo():
        return 1
    else:
        return 0
