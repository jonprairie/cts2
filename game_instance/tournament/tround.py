import cts2.util.stringtable as stringtable
import cts2.game_instance.tournament.chessgame.game as game

class tround:
    """tournament round"""

    def __init__(self, player_list, pairings, round_num):
        self.round_num = round_num
        self.is_finished = False
        self.game_list = [
            game.game(
                player_list[p[0]],
                player_list[p[1]]
            ) for p in pairings if (
                p[0] != 'bye' and p[1] != 'bye'
            )
        ]
        self.bye_list = [
            player_list[p[n]] for n in range(2) for p in pairings
            if (
                p[n] != 'bye' and p[abs(n-1)] == 'bye'
            )
        ]
        self.round_st = stringtable.stringtable(
            "round " + str(round_num),
            self.game_list,
            footer="\n".join(
                'bye: ' + str(b) for b in self.bye_list
            )
        )

    def __str__(self):
        return str(self.round_st)

    def Simulate(self):
        self.is_finished = True
        for g in self.game_list:
            g.Simulate()
