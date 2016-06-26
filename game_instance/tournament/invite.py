class invite:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def Accept(self):
        self.sender.AcceptInvitation(self)

    def Decline(self):
        self.sender.DeclineInvitation(self)
