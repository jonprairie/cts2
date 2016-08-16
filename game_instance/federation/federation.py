import cts2.game_instance.federation.tournamentdirector as tournamentdirector
import random


class federation:
    def __init__(self, api, country):
        self.api = api
        self.country = country

        self.td_list = []
        for i in range(random.randint(1, 4)):
            temp_td = tournamentdirector.tournamentdirector(
                self.api,
                self.country
            )
            self.td_list.append(temp_td)
