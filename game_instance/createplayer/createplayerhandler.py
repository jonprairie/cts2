import cts2.util.pkg as pkg
import cts2.game_instance.createplayer.genplayer as genplayer


class createplayerhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "create_player_handler",
            [
                "gen_player",
                "gen_player_list"
            ],
            ["def_options"]
        )

    def Activate(self):
        self.default_options = self.api.Call(
            "def_options",
            [
                "play_strength_mu",
                "play_strength_sigma"
            ]
        )

    def GenPlayer(self):
        return genplayer.GenPlayer(self.default_options)

    def GenPlayerList(self, num_players=1):
        return [
            genplayer.GenPlayer(
                self.default_options
            ) for p in range(num_players)
        ]
