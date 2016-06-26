import cts2.application.util.eventprocessor as eventprocessor
import cts2.application.util.maintenancesubscriber as maintenancesubscriber
import cts2.application.util.stringtable as stringtable
import cts2.application.events.createplayerlist as createplayerlist
import cts2.application.events.createplayer as createplayer

class playerhandler(
    eventprocessor.eventprocessor,
    maintenancesubscriber.maintenancesubscriber
):

    def __init__(self, event_handler):

		# initialize module as an eventprocessor
        self.event_dict = dict(
            get_player_list=self.GetPlayersEv
        )
        eventprocessor.eventprocessor.__init__(
            self,
            self.event_dict,
            event_handler
        )
        maintenancesubscriber.maintenancesubscriber.__init__(
            self, True, False, False, False
        )

        self.create_players_event = createplayerlist.createplayerlist(
            self.default_options["num_initial_cpu_players"]
        )
        self.create_player_event = createplayer.createplayer()

        self.player_list = []
        self.num_players = self.default_options["num_initial_cpu_players"]
        self.InitPlayers()

    def InitPlayers(self):
        self.event_handler.ProcessEvent(self.create_players_event)
        self.player_list = self.create_players_event.player_list

    def GetNumPlayers(self):
        return self.num_players

    def GetPlayersEv(self, ev):
        ev.player_list = self.GetPlayers()[:]

    #Get Functions
    def GetPlayers(self):
        return self.player_list

    #Maintenance Functions
    #def RegisterForTournaments(self):
    #    tournament_list = self.tournament_handler.GetNewTournaments()
    #    for p in self.player_list:
    #        p.RegisterForTournaments(tournament_list)

    def DailyMaintenance(self, date):
        # self.RegisterForTournaments()
        for p in self.player_list:
            p.ProcessInvites()

def PlayerCMP(player_x, player_y):
    """returns -1 if player_x's elo is greater than player_y's elo, 0 if they are equal, and 1 otherwise"""

    if player_x.GetElo() > player_y.GetElo():
        return -1
    elif player_y.GetElo() > player_x.GetElo():
        return 1
    else:
        return 0
