import random


class tournamentdirector:
    def __init__(self, tournament, recruiter, scheduler):
        self.tournament = tournament
        self.recruiter = recruiter
        self.scheduler = scheduler
        self.tournament.SetWorstCaseDateRange(
            self.scheduler.GetMaxNumberRounds(
                self.recruiter.GetMaxPlayers()
            )
        )

    def Maintenance(self, date):
        if int(self.tournament.start_julian_date) == int(date):
            if self.recruiter.HasEnoughPlayers():
                self.recruiter.CloseRecruiting()
                self.scheduler.Start(self.recruiter.GetRecruits())
                self.tournament.Start(
                    self.recruiter.GetRecruits(),
                    self.scheduler.GetSchedule()
                )
            else:
                self.tournament.CancelTournament()

        if not self.tournament.IsCancelled():
            if not self.tournament.IsStarted():
                self.recruiter.Recruit()
                self.tournament.AddPlayerList(self.recruiter.GetRecruits())
            elif not self.tournament.IsFinished():
                if self.tournament.PlaysToday(date):
                    self.tournament.GetSchedule().BuildRoundSchedule()
                    self.PlayRound()
                elif int(date) > max(self.tournament.GetDateRange()):
                    raise Exception(
                        """%s: current date (%s) is outside tournament
                        date range %s""" % (
                            self.tournament.name,
                            str(date),
                            str(self.tournament.GetDateRange())
                        )
                    )

    def PlayRound(self):
        current_round = self.tournament.GetSchedule().GetCurrentRound()
        self.tournament.GetSchedule().SimulateCurrentRound()
        self.tournament.history.AddRound(current_round)
        if self.tournament.GetSchedule().IsFinished():
            self.tournament.champion = self.tournament.history.GetLeader()
            self.tournament.Finish()

