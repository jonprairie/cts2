import cts2.util.pkg as pkg
import cts2.game_instance.federation.federation as federation


class federationhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "federation_handler",
            ["federation_handler_dummy"],
            ["get_country_list"],
            save_ind=True
        )
        self.federation_list = []

    def Activate(self):
        # TODO: figure out a way to implement global federation
        pass
        # country_list = self.api.Call("get_country_list")
        # self.federation_list = [
        #     federation.federation(self, c) for c in country_list
        # ]
