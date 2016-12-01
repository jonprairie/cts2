import random

class temp_inv_eval:
    def EvalInvite(self, player, invite):
        if not player.pth.TournamentConflicts(invite.GetSender()):
            return random.choice([0,0,0,1])
        else:
            return False
            
class playerdriver:
    def __init__(self, player, tournament_invite_evaluator, inbox, outbox):
        self.player = player
        self.tournament_invite_evaluator = tournament_invite_evaluator
        self.inbox = inbox
        self.outbox = outbox

    def DailyMaintenance(self, date):
        self.player.DailyMaintenance()
        self.ProcessInvites()

    def MonthlyMaintenance(self, date):
        self.UpdateElo()

    def ProcessInvites(self):
        for invite in self.inbox.GetMessages():
            if self.tournament_invite_evaluator.EvalInvite(self.player, invite):
                invite.Accept()
                self.player.AddTournament(invite.GetSender())
            else:
                invite.Decline()
        self.inbox.PurgeMessages()

    def UpdateElo(self):
        self.player.SetElo(self.player.GetLiveElo())
