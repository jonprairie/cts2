import random
import cts2.game_instance.tournament.tround as tround
import tournamentschedule


class roundrobinschedule(tournamentschedule.tournamentschedule):
    def __init__(self):
        tournamentschedule.tournamentschedule.__init__(self)
        self.first_call_to_build = True

    def BuildRoundSchedule(self):
        if self.first_call_to_build:
            self.first_call_to_build = False
            pairings = self.BuildFullPairings(len(self.player_list))
            for round_num, round_pairings in enumerate(pairings):
                self.rounds.append(
                    tround.tround(
                        self.player_list,
                        round_pairings,
                        round_num+1
                    )
                )
            random.shuffle(self.rounds)
            # TODO: fix this hack :/
            for round_num, round in enumerate(self.rounds):
                round.round_num = round_num + 1
                round.round_st = round.BuildStringTable()

    def GetType(self):
        return "round_robin"

    def GetNumRounds(self):
        #TODO: and this one
        num_players = len(self.player_list)
        if num_players % 2 == 1:
            num_byes = 1
        else:
            num_byes = 2
        return 2*(num_players+num_byes-1)

    def GetMaxNumberRounds(self, max_players):
        if max_players % 2 == 1:
            num_byes = 1
        else:
            num_byes = 2
        return 2*(max_players+num_byes-1)

    def BuildFullPairings(self, num_players):
        """
        returns a list of lists of round pairings, as indexes
        into the player list.

            for example, if there are 6 players this Functions
            will return something like the following list:
                [
                    [ # round 1
                        [0,2], [1,3], ['bye',4], ['bye',5]
                    ],
                    [ # round 2
                        [3,0], [4,2], [5,1], ['bye','bye']
                    ],
                    # ...etc
                ]
        """

        num_byes = 0
        odd = num_players % 2
        player_list = range(num_players)

        if odd:
            num_byes = 1
        else:
            num_byes = 2

        fixed = [0]
        top = range(
            1,
            num_players//2-(abs(odd-1))
        )
        top.extend(['bye' for b in range(num_byes)])
        bottom = range(
            num_players//2-(abs(odd-1)),
            num_players
        )

        full_pairings = []
        top_is_white = True

        self.num_rounds = 2*(num_players+num_byes-1)
        for r in range(self.num_rounds):
            if top_is_white:
                t_top = fixed[:]
                t_top.extend(top)
                round_pairings = [
                    (t_top[i], bottom[i]) for i in range(len(bottom))
                ]
            else:
                t_top = fixed[:]
                t_top.extend(top)
                round_pairings = [
                    (bottom[i], t_top[i]) for i in range(len(bottom))
                ]

            full_pairings.append(round_pairings)
            top.insert(0, bottom[0])
            bottom.append(top[num_players//2])
            top.remove(top[num_players//2])
            bottom.remove(bottom[0])
            top_is_white = not top_is_white

        return full_pairings

