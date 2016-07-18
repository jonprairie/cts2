import cts2.application.events.messageevent as messageevent
import cts2.application.util.maintenancesubscriber as maintenancesubscriber
import random


class tournamentdirector(maintenancesubscriber.maintenancesubscriber):
    def __init__(self, api):
        self.api = api
        self.start_julian_date = random.randint(1, 365)
        self.current_tournament = False

    def WeeklyMaintenance(self, date):
        if not self.current_tournament:
            self.current_tournament = self.api.CreateTournament(
                self.start_julian_date,
                offset=False
            )
