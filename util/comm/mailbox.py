"""
class to abstract the receiving of messages
"""


class mailbox:
    def __init__(self):
        self.inbox = dict()

    def AddInbox(self, k):
        self.inbox.update([(k, [])])

    def AddMessage(self, k, msg):
        if k in self.inbox:
            self.inbox[k].append(msg)
        else:
            self.AddInbox(k)
            self.AddMessage(k, msg)

    def GetMail(self, k):
        if k in self.inbox:
            return self.inbox[k]
        else:
            return []

    def DeleteMessage(self, k, msg):
        if msg in self.inbox[k]:
            self.inbox[k].remove(msg)
