import event

class getplayerlist(event.event):
    def __init__(self):
        event.event.__init__(self, "get_player_list")
        self.player_list = []
