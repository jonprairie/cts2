import event

class createplayerlist(event.event):
    def __init__(self, num_players):
        event.event.__init__(self, "create_player_list")
        self.num_players = num_players
        self.player_list = False
