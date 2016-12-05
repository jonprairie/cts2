class outbox:
    def __init__(self, owner, get_inboxes, close):
        self.owner = owner
        self.get_inboxes = get_inboxes
        self.close = close

    def SendMessage(self, inbox_key, msg):
        self.get_inboxes()[inbox_key].SendMessage(msg)

    def GetInboxes(self):
        return self.get_inboxes()

    def GetAddressBook(self):
        return self.GetInboxes().keys()

    def Close(self):
        self.close()
