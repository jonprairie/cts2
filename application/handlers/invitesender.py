import cts2.application.util.eventprocessor as eventprocessor
import cts2.application.util.maintenancesubscriber as maintenancesubscriber
import cts2.application.events.messageevent as messageevent

class invitesender(
    eventprocessor.eventprocessor,
    maintenancesubscriber.maintenancesubscriber
):

    def __init__(self, event_handler):
        eventprocessor.eventprocessor.__init__(self,dict(),event_handler)
        maintenancesubscriber.maintenancesubscriber.__init__(
            self, True, False, False, False
        )
        self.get_tournament_list = messageevent.messageevent(
            "get_non_started_tournament_list"
        )
        self.get_player_list = messageevent.messageevent(
            "get_player_list"
        )

    def GetTournamentList(self):
        self.event_handler.ProcessEvent(self.get_tournament_list)
        return self.event_handler.tournament_list

    def GetPlayerList(self):
        self.event_handler.ProcessEvent(self.get_player_list)
        return self.event_handler.player_list

    def DailyMaintenance(self, date):
        tourn_list = self.GetTournamentList()
        player_list = self.GetPlayerList()
        open_tourn_list = filter(
            lambda t: return not t.open_tournament,
            tourn_list
        )
        for t in open_tourn_list:
            pass
