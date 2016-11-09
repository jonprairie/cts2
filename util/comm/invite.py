class invite:
    def __init__(self, sender, receiver, sender_proxy=None):
        self.sender = sender
        self.sender_proxy = sender_proxy
        self.receiver = receiver

    def Accept(self):
        if self.sender_proxy:
            self.sender_proxy.AcceptInvitation(self)
        else:
            self.sender.AcceptInvitation(self)

    def Decline(self):
        if self.sender_proxy:
            self.sender_proxy.DeclineInvitation(self)
        else:
            self.sender.DeclineInvitation(self)
