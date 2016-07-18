import cts2.application.util.row as row
import cts2.stats.gamesim as gamesim

class game(row.row):
    def __init__(self, white, black):
        self.white = white
        self.black = black
        self.is_finished = False
        self.result = ""
        self.result_obj = None
        self.white_score = None
        self.black_score = None
        row.row.__init__(
            self,
            dict(
                white=self.white,
                black=self.black,
                result=self.result
            )
        )

    def __str__(self):
        return self.result+str(self.white)+" - "+str(self.black)

    def Simulate(self):
        self.is_finished = True
        self.result_obj = gamesim.SimulateResult(
            self.white.GetPlayStrength(),
            self.black.GetPlayStrength()
        )
        rate_adj_wht, rate_adj_blk = gamesim.RatingAdjustment(
            self.white.GetPlayStrength(),
            self.black.GetPlayStrength(),
            self.result_obj
        )
        self.white.UpdateLiveElo(rate_adj_wht)
        self.black.UpdateLiveElo(rate_adj_blk)
        self.UpdateRow(
            "result",
            self.result_obj.ToString()
        )

    def BlackWins(self):
        self.is_finished = True
        self.result = "  0 - 1  "
        self.white_score = 0
        self.black_score = 2
        self.UpdateRow("result",self.result)

    def WhiteWins(self):
        self.is_finished = True
        self.result = "  1 - 0  "
        self.white_score = 2
        self.black_score = 0
        self.UpdateRow("result",self.result)

    def Draw(self):
        self.is_finished = True
        self.result = "1/2 - 1/2"
        self.black_score = 1
        self.white_score = 1
        self.UpdateRow("result",self.result)
