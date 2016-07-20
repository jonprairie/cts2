import cts2.game_instance.tournament.tround as tround
import cts2.application.util.stringtable as stringtable


class singlematch:
    def __init__(self, bestof=5):
        self.schedule_finished = False
        self.schedule = []
        self.bestof = bestof

    def BuildSchedule(self):
        self.schedule_finished = True
        self.current_round_index = 0
        pairings = self.BuildFullPairings(self.bestof)
        for round_num, round_pairings in enumerate(pairings):
            self.schedule.append(
                tround.tround(
                    self.player_list,
                    round_pairings,
                    round_num+1
                )
            )
        self.current_round = self.schedule[
            self.current_round_index
        ]
        return self.schedule

    def BuildFullPairings(self, bestof):
        ret_list = []
        for r in range(bestof):
            if r % 2:
                ret_list.append([(1, 0)])
            else:
                ret_list.append([(0, 1)])
        return ret_list
