import random


class tournamentdirector:
    def __init__(self, api):
        self.api = api
        self.start_julian_date = random.randint(1, 365)
        self.tournament_list = []

    def WeeklyMaintenance(self, date):
        if self.TimeForNewTournament(date):
            self.start_julian_date = self.start_julian_date + 365
            self.tournament_list.append(
                self.api.CreateTournament(
                    self.start_julian_date,
                    offset=False
                )
            )

    def GetCurrentTournament(self):
        return self.tournament_list[-1]

    def GetChampion(self, seq=0):
        return self.tournament_list[-seq]

    def TimeForNewTournament(self, date):
        if date - self.start_julian_date > 200:
            return True
        else:
            return False
