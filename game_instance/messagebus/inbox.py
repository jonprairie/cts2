class inbox:
    def __init__(self, owner, close):
        self.owner = owner
        self.messages = []
        self.close = close

    def GetOwner(self):
        return self.owner

    def SendMessage(self, msg):
        self.messages.append(msg)

    def GetMessages(self):
        return self.messages
    
    def PurgeMessages(self):
        self.messages = []

    def Close(self):
        self.close()
