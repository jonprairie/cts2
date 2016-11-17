import random
import cts2.game_instance.tournament.tround as tround
import tournamentschedule


class matchschedule(tournamentschedule.tournamentschedule):
    def __init__(self, num_rounds):
        tournamentschedule.tournamentschedule.__init__(
            self,
            num_rounds=num_rounds
        )
        self.first_call_to_build = True

    def BuildRoundSchedule(self):
        if self.first_call_to_build:
            self.first_call_to_build = False
            pairings = self.BuildFullPairings()
            for round_num, round_pairings in enumerate(pairings):
                self.rounds.append(
                    tround.tround(
                        self.player_list,
                        round_pairings,
                        round_num+1
                    )
                )

    def GetNumRounds(self):
        return self.num_rounds

    def GetMaxNumberRounds(self, max_players):
        return self.num_rounds

    def BuildFullPairings(self):
        first_white = random.randint(0,1)
        first_pairing = [first_white, (first_white+1)%2]
        return [
            [[
                (first_pairing[0]+round_num)%2,
                (first_pairing[1]+round_num)%2
            ]] for round_num in range(1,self.num_rounds+1)
        ]

    def GetMandatoryPlayerRange(self):
        return (2, 2)




