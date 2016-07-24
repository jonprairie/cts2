import cts2.util.pkg as pkg
import cts2.game_instance.federation.federation as federation
import cts2.game_instance.federation.country as country


class federationhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "federation_handler",
            ["federation_handler_dummy"],
            ["register_for_maintenance"],
            save_ind=True
        )

    def Activate(self):
        self.api.Call("register_for_maintenance", self, ["weekly"])
        self.federation_list = []
        self.global_federation = federation.federation(
            self,
            country.world
        )
        for cntry in country.country_list:
            self.federation_list.append(
                federation.federation(
                    self,
                    cntry
                )
            )

    def WeeklyMaintenance(self, dte):
        for tdir in self.global_federation.td_list + [
            td for fed in self.federation_list for td in fed.td_list
        ]:
            tdir.WeeklyMaintenance(dte)

    def CreateTournament(self, *args, **kwargs):
        return self.api.Call("create_tournament", *args, **kwargs)
