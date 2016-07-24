import random


class invitereceiver:
    def __init__(self):
        self.pending_invites = []
        self.accepted_invites = []

    def AddInvite(self, inv):
        self.pending_invites.append(inv)

    def ProcessInvites(self):
        for inv in self.pending_invites:
            if self.EvaluateInvite(inv):
                self.AcceptInvitation(inv)
            else:
                self.DeclineInvitation(inv)

    def AcceptInvitation(self, inv):
        inv.sender.AcceptInvitation(inv)
        self.accepted_invites.append(inv)
        self.pending_invites.remove(inv)
        self.AcceptCleanUp(inv)

    def AcceptCleanUp(self, inv):
        pass

    def DeclineInvitation(self, inv):
        inv.sender.DeclineInvitation(inv)
        self.pending_invites.remove(inv)

    def EvaluateInvite(self, inv):
        if random.randint(1, 100) < 25:
            return True
        else:
            return False
