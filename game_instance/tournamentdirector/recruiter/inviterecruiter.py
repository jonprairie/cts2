import cts2.util.comm.invitesender as invitesender
import random

class inviterecruiter(invitesender.invitesender):
    def __init__(self, tournament, player_range, player_polling_function):
        invitesender.invitesender.__init__(self, player_range)
        self.tournament = tournament
        self.player_range = player_range
        self.player_polling_function = player_polling_function

    def Recruit(self):
        while not self.InvitesFull():
            player = random.choice(
                self.player_polling_function()
            )
            self.SendInvite(player, inviter=self.tournament)

    def GetRecruits(self):
        return self.player_list

    def HasEnoughPlayers(self):
        return len(self.player_list) in range(
            self.player_range[0], self.player_range[1]+1
        )

    def GetMaxPlayers(self):
        return self.player_range[1]
