"""
representation of a tournament's progression through the
rounds of its schedule.

main interactions are through the following methods:
AddRound     - add round results to history
GetStandings - retrieve standings
GetLeader    - retrieve player leading the tournament
"""
import cts2.util.stringtable as stringtable
import cts2.util.row as row
import playerresult


class tournamenthistory:
    def __init__(self, player_list):
        self.pr_dict = dict([
            (p, playerresult.playerresult(p)) for p in player_list
        ])
        self.rounds = []
        self.history_snapshots = []

    def AddRound(self, r):
        if r not in self.rounds:
            self.history_snapshots.append(self.GetStandings())
            self.rounds.append(r)
            for g in r.GetGames():
                self.pr_dict[g.white].AddGame(g)
                self.pr_dict[g.black].AddGame(g)

    def GetPlayerResult(self, player):
        if p in self.pr_dict:
            return self.pr_dict[p]
        else:
            return None

    def GetStandings(self, offset=0):
        if offset == 0:
            return stringtable.stringtable(
                "tournament standings",
                sorted(self.pr_dict.values(), reverse=True)
            )
        else:
            key = offset % -len(self.history_snapshots)
            return self.history_snapshots[key]

    def GetLeader(self):
        return sorted(self.pr_dict.values())[-1].player
