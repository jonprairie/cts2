import cts2.application.events.messageevent as messageevent
import cts2.application.util.maintenancesubscriber as maintenancesubscriber
import random

class tournamentdirector(maintenancesubscriber.maintenancesubscriber):
    def __init__(self, event_handler):
        self.event_handler = event_handler
        maintenancesubscriber.maintenancesubscriber.__init__(
            self, False, True, False, False
        )
        self.start_julian_date = random.randint(1,365)
        self.create_tourn_event = messageevent.messageevent(
            "create_tournament"
        )
        self.create_tourn_event.start_julian_date = self.start_julian_date
        self.current_tournament = False

    def WeeklyMaintenance(self, date):
        if not self.current_tournament:
            self.event_handler.ProcessEvent(
                self.create_tourn_event
            )
            self.current_tournament = self.create_tourn_event.new_tournament
