class openrecruiter:
    def __init__(self, tournament, player_range, inbox):
        self.tournamnent = tournament
        self.player_range = player_range
        self.inbox = inbox
        self.player_list = []

    def Recruit(self):
        for invite in self.inbox.GetMessages():
            if not self.IsFull():
                invite.Accept()
                self.player_list.append(invite.GetSender())
            else:
                invite.Decline()
        self.inbox.PurgeMessages()

    def CloseRecruiting(self):
        self.inbox.Close()

    def IsFull(self):
        return len(self.player_list) >= self.GetMaxPlayers()
    
    def GetRecruits(self):
        return self.player_list

    def HasEnoughPlayers(self):
        return len(self.player_list) in range(
            self.player_range[0], self.player_range[1]
        )

    def GetMaxPlayers(self):
        return self.player_range[1]
