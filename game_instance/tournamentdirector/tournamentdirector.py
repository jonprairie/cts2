import random


class tournamentdirector:
    def __init__(self, tournament, recruiter, scheduler):
        self.tournament = tournament
        self.recruiter = recruiter
        self.scheduler = scheduler

    def Maintenance(self, date):
        if int(self.tournament.start_julian_date) == int(date):
            if self.recruiter.HasEnoughPlayers():
                self.scheduler.Start(self.recruiter.GetRecruits())
                self.tournament.Start(
                    self.recruiter.GetRecruits(),
                    self.scheduler.GetNumRounds()
                )
            else:
                self.tournament.CancelTournament()

        if not self.tournament.IsCancelled():
            if not self.scheduler.IsStarted():
                self.recruiter.Recruit()
            elif not self.scheduler.IsFinished():
                if self.tournament.PlaysToday(date):
                    self.scheduler.BuildRoundSchedule()
                    self.PlayRound()
            elif not self.tournament.finished:
                self.tournament.Finish()

    def PlayRound(self):
        current_round = self.scheduler.GetCurrentRound()
        self.scheduler.SimulateCurrentRound()
        self.tournament.history.AddRound(current_round)
        if self.scheduler.IsFinished():
            self.tournament.champion = self.tournament.history.GetLeader()

