import cts2.game_instance.federation.tournamentdirector as tournamentdirector
import random

class federation:
    def __init__(self, event_handler, country):
        self.event_handler = event_handler
        self.country = country

        self.td_list = []
        for i in range(random.randint(1,4)):
            temp_td = tournamentdirector.tournamentdirector(self.event_handler)
            self.td_list.append(temp_td)
