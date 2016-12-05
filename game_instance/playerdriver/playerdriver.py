import cts2.util.comm.invite as invite
import random

class temp_inv_eval:
    def EvalTournament(self, tournament, player):
        return random.choice([0,0,0,1])
            
class playerdriver:
    def __init__(self, player, tournament_evaluator, inbox, outbox):
        self.player = player
        self.tournament_evaluator = tournament_evaluator
        self.inbox = inbox
        self.outbox = outbox
        self.open_applications = []

    def DailyMaintenance(self, date):
        self.player.DailyMaintenance()
        self.ProcessInvites()
        self.SearchForTournaments()

    def MonthlyMaintenance(self, date):
        self.UpdateElo()

    def ProcessInvites(self):
        for invite in self.inbox.GetMessages():
            if not self.TournamentConflicts(invite.GetSender()): 
                if self.tournament_evaluator.EvalTournament(invite.GetSender(), self.player):
                    invite.Accept()
                    self.player.AddTournament(invite.GetSender())
                else:
                    invite.Decline()
            else:
                invite.Decline()
        self.inbox.PurgeMessages()

    def SearchForTournaments(self):
        tournament_list = self.outbox.GetAddressBook()
        if tournament_list:
            for n in range(random.randint(0,5)):
                potential_tournament = random.choice(tournament_list)
                if not self.TournamentConflicts(potential_tournament):
                    if self.tournament_evaluator.EvalTournament(
                        potential_tournament,
                        self.player
                    ):
                        self.outbox.SendMessage(
                            potential_tournament,
                            invite.invite(
                                self.player,
                                potential_tournament
                            )
                        )

    def TournamentConflicts(self, tournament):
        if self.player.pth.TournamentConflicts(tournament):
            return True
        else:
            pending_tournaments = [app.GetReceiver() for app in self.open_applications]
            for tourn in pending_tournaments:
                if tourn.Conflicts(tournament):
                    return True
        return False

    def UpdateElo(self):
        self.player.SetElo(self.player.GetLiveElo())
