import cts2.util.pkg as pkg
import cts2.game_instance.federation.federation as federation


class federationhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "federation_handler",
            ["federation_handler_dummy"],
            [
                "register_for_maintenance",
                "get_country_list"
            ],
            save_ind=True
        )

    def Activate(self):
        # TODO: figure out a way to implement global federation
        self.api.Call("register_for_maintenance", self, ["weekly"])
        country_list = self.api.Call("get_country_list")
        self.federation_list = [
            federation.federation(self, c) for c in country_list
        ]

    def WeeklyMaintenance(self, dte):
        for tdir in [
            td for fed in self.federation_list for td in fed.td_list
        ]:
            tdir.WeeklyMaintenance(dte)

    def CreateTournament(self, *args, **kwargs):
        return self.api.Call("create_tournament", *args, **kwargs)
