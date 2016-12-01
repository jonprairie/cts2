import random
import invite


class invitesender:
    def __init__(self, (_, max_invites)):
        self.max_invites = max_invites

        self.open_invites = []
        self.players_invited = []

        self.player_list = []

    # TODO: fix invites, this is a bit hackish
    def SendInvite(self, inviter, player):
        if player not in self.players_invited:
            self.players_invited.append(player)
            if self.Thresher(player):
                inv = invite.invite(
                    inviter,
                    player
                )
                player.AddInvite(inv)
                self.open_invites.append(inv)
                return True
        return False

    def Thresher(self, player):
        if random.randint(1,100) < 35:
            return True
        else:
            return False

    def InvitesFull(self):
        potential_players = len(self.open_invites) + len(self.player_list)
        return potential_players >= self.max_invites

    def AcceptInvitation(self, inv):
        self.open_invites.remove(inv)
        if inv.receiver not in self.player_list:
            self.AddPlayer(inv.receiver)

    def DeclineInvitation(self, inv):
        self.open_invites.remove(inv)

    def AddPlayer(self, player):
        self.player_list.append(player)
