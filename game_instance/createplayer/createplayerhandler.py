import cts2.application.util.pkg as pkg
import genplayer


class createplayerhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "create_player_handler",
            [
                "gen_player",
                "gen_player_list"
            ]
        )
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
            genplayer.GenPlayer(self.default_options) for p in num_players
        ]
