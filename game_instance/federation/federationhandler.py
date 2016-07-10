import cts2.application.util.pkg as pkg
import cts2.game_instance.federation.federation as federation
import cts2.game_instance.federation.country as country


class federationhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "federation_handler",
            [],
            []
        )
        self.federation_list = []
        self.global_federation = federation.federation(
            self.event_handler,
            country.world
        )
        for cntry in country.country_list:
            self.federation_list.append(
                federation.federation(
                    self.event_handler,
                    cntry
                )
            )
