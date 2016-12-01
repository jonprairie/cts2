class outbox:
    def __init__(self, owner, get_inboxes):
        self.owner = owner
        self.get_inboxes = get_inboxes

    def SendMessage(self, inbox_key, msg):
        self.get_inboxes()[inbox_key].SendMessage(msg)
