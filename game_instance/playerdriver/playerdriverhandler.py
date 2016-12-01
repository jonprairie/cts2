"""
handles processing and maintenance of playerdrivers
"""
import cts2.util.pkg as pkg
import playerdriver

class playerdriverhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "player_driver_handler",
            [
                "create_random_player_driver",
                "get_player_driver_list"
            ],
            [
                "register_for_maintenance",
                "create_random_player",
                "create_player_inbox",
                "create_player_outbox",
                "def_options"
            ],
            save_ind = True
        )
        self.player_driver_list = []

    def Activate(self):
        self.api.Call("register_for_maintenance", self, ["daily", "monthly"])
        self.default_options = self.api.Call(
            "def_options",
            ["num_initial_cpu_players"]
        )
        for p in range(self.default_options["num_initial_cpu_players"]):
            self.CreateRandomPlayerDriver()

    def GetPlayerDriverList(self):
        return self.player_driver_list

    def CreateRandomPlayerDriver(self):
        player = self.api.Call("create_random_player")
        player_inv_eval = playerdriver.temp_inv_eval()
        player_inbox = self.api.Call("create_player_inbox", player)
        player_outbox = self.api.Call("create_player_outbox", player)
        temp_player_driver = playerdriver.playerdriver(
            player,
            player_inv_eval,
            player_inbox,
            player_outbox
        )
        self.player_driver_list.append(temp_player_driver)
        return temp_player_driver

    def DailyMaintenance(self, dte):
        for player_driver in self.player_driver_list:
            player_driver.DailyMaintenance(dte)

    def MonthlyMaintenance(self, dte):
        for player_driver in self.player_driver_list:
            player_driver.MonthlyMaintenance(dte)
