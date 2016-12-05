import cts2.util.comm.invite as invite
import random


class inviterecruiter:
    def __init__(self, tournament, player_range, outbox, player_polling_fn):
        self.player_range = player_range
        self.tournament = tournament
        self.player_range = player_range
        self.outbox = outbox
        self.player_polling_fn = player_polling_fn
        self.open_invites = []
        self.players_invited = []
        self.player_list = []

    def Recruit(self):
        self.CleanOpenInvites()
        self.SendOpenInvites()

    def CleanOpenInvites(self):
        for inv in self.open_invites:
            if inv.IsAccepted():
                self.AddPlayer(inv.GetReceiver())
                self.open_invites.remove(inv)
            elif inv.IsDeclined():
                self.open_invites.remove(inv)

    def SendOpenInvites(self):
        while not self.InvitesFull():
            player = random.choice(
                self.player_polling_fn()
            )
            self.SendInvite(self.tournament, player)

    def GetRecruits(self):
        return self.player_list

    def CloseRecruiting(self):
        self.outbox.close()

    def HasEnoughPlayers(self):
        return len(self.player_list) in range(
            self.player_range[0], self.player_range[1]+1
        )

    def GetMaxPlayers(self):
        return self.player_range[1]

    def SetPlayerRange(self, player_range):
        self.player_range = player_range

    def SendInvite(self, inviter, player):
        if player not in self.players_invited:
            self.players_invited.append(player)
            if self.Thresher(player):
                inv = invite.invite(
                    inviter,
                    player
                )
                self.outbox.SendMessage(player, inv)
                self.open_invites.append(inv)
                return True
        return False

    def Thresher(self, player):
        return random.randint(1,100) < 35

    def InvitesFull(self):
        potential_players = len(self.open_invites) + len(self.player_list)
        return potential_players >= self.GetMaxPlayers()

    def AddPlayer(self, player):
        self.player_list.append(player)
