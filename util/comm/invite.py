class invite:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.accepted = False
        self.declined = False

    def Accept(self):
        self.accepted = True

    def Decline(self):
        self.declined = True

    def IsAccepted(self):
        return self.accepted

    def IsDeclined(self):
        return self.declined

    def GetSender(self):
        return self.sender

    def GetReceiver(self):
        return self.receiver
