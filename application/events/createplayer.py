import event

class createplayer(event.event):
    def __init__(self):
        event.event.__init__(self, "create_player")
        self.player = False
