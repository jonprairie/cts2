"""
representation of a player's results.

Also includes a cmp function called prcmp which can
compare two player results against each other.

primary interactions occur through the following methods:
AddGame - add game to player results
GetScore - get player score in tournament
GetStringTable - get stringtable representation of results

future enhancements:
tiebreakers
"""
import cts2.util.row as row
import cts2.util.stringtable as stringtable


class playerresult(row.row):
    def __init__(self, p):
        self.player = p
        self.game_list = []
        self.total_score = 0
        row.row.__init__(
            self,
            dict(
                player=p.InvertName(),
                score="0/0",
                elo=p.GetElo(strng=True),
                live_elo=p.GetLiveElo(strng=True)
            )
        )

    def __cmp__(self, other):
        # if len(pr1.game_list) == len(pr2.game_list):
        if (
            int(round(self.GetScore()*2, 0)) ==
            int(round(other.GetScore()*2, 0))
        ):
            return self.ResolveTiebreaks(other)
        elif self.GetScore() < other.GetScore():
            return -1
        else:
            return 1

    def ResolveTiebreaks(self, other):
        return 0

    def AddGame(self, g):
        self.game_list.append(g)
        if self is g.GetWhite():
            self.total_score += g.GetResult().WhiteResult()
        else:
            self.total_score += g.GetResult().BlackResult()
        self.UpdateRow(
            "score",
            str(round(self.total_score, 1)) + "/" +
            str(len(self.game_list))
        )
        self.UpdateRow(
            "live_elo",
            self.player.GetLiveElo(strng=True)
        )

    def GetScore(self):
        return self.total_score

    def GetStringTable(self):
        return stringtable.stringtable(
            self.player.InvertName() + " results",
            self.game_list
        )
