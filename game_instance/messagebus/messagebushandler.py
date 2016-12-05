import cts2.util.pkg as pkg
import inbox
import outbox

class messagebushandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "message_bus_handler",
            [
                "create_player_inbox",
                "create_player_outbox",
                "create_tournament_inbox",
                "create_tournament_outbox",
                "destroy_tournament_inbox",
                "destroy_tournament_outbox"
            ],
            [],
            save_ind = True
        )
        self.tournament_inbox_dict = dict()
        self.tournament_outbox_dict = dict()
        self.player_inbox_dict = dict()
        self.player_outbox_dict = dict()

    def GetTournamentInboxDict(self):
        return self.tournament_inbox_dict

    def GetPlayerInboxDict(self):
        return self.player_inbox_dict

    def CreatePlayerInbox(self, player):
        temp_inbox = inbox.inbox(player, lambda: self.DestroyPlayerInbox(player))
        self.player_inbox_dict.update([(player, temp_inbox)])
        return temp_inbox

    def CreatePlayerOutbox(self, player):
        temp_outbox = outbox.outbox(
            player,
            self.GetTournamentInboxDict,
            lambda: self.DestroyPlayerOutbox(player)
        )
        self.player_outbox_dict.update([(player, temp_outbox)])
        return temp_outbox

    def CreateTournamentInbox(self, tournament):
        temp_inbox = inbox.inbox(tournament, lambda: self.DestroyTournamentInbox(tournament))
        self.tournament_inbox_dict.update([(tournament, temp_inbox)])
        return temp_inbox

    def CreateTournamentOutbox(self, tournament):
        temp_outbox = outbox.outbox(
            tournament,
            self.GetPlayerInboxDict,
            lambda: self.DestroyTournamentOutbox(tournament)
        )
        self.tournament_outbox_dict.update([(tournament, temp_outbox)])
        return temp_outbox

    def DestroyTournamentInbox(self, tournament):
        self.tournament_inbox_dict.pop(tournament, None)

    def DestroyTournamentOutbox(self, tournament):
        self.tournament_outbox_dict.pop(tournament, None)

    def DestroyPlayerInbox(self, player):
        self.player_inbox_dict.pop(player, None)

    def DestroyPlayerOutbox(self, player):
        self.player_outbox_dict.pop(player, None)
