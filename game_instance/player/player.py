"""
representation of a chess player
"""
import cts2.util.comm.invitereceiver as invitereceiver
import cts2.util.row as row
import playertournamenthandler
import numgenerator


class player(
    invitereceiver.invitereceiver,
    row.row
):
    """chess player"""

    def __init__(
        self, first_name, last_name, age,
        gender="male", country=None, title=None,
        elo=2500, play_strength=2500, fame=2500,
        player_type="cpu"
    ):

        self.player_num = numgenerator.num_gen.GenNum()
        self.first_name = first_name    #player's first name
        self.last_name = last_name      #player's last name
        self.age = age                  #player's age
        self.gender = gender
        self.country = country
        self.title = title              #player's title
        self.elo = float(elo)           #player's elo
        self.live_elo = float(elo)
        self.chess_federation = 0
        self.play_strength = play_strength

        self.player_type = player_type   #computer, human, bye

        self.tournament_invites = []
        self.pth = playertournamenthandler.playertournamenthandler()

        invitereceiver.invitereceiver.__init__(self)
        row.row.__init__(
            self,
            dict(
                player=self.InvertName(),
                age=self.age,
                country=self.country.GetShortName(),
                elo=self.GetElo(strng=True),
                live_elo=self.GetLiveElo(strng=True)
            )
        )

    # Get Functions
    def __str__(self):
        return self.last_name + ", " + self.first_name

    def GetPlayerNum(self):
        return self.player_num

    def GetType(self):
        return self.player_type

    def GetName(self, invert=0):
        name = ""
        if invert:
            name = self.last_name + ", " + self.first_name
        else:
            name = self.first_name + " " + self.last_name
        return name

    def GetGender(self):
        return self.gender

    def GetCountry(self):
        return self.country

    def GetElo(self, strng=False):
        """returns official elo."""
        if strng:
            return "{0:.1f}".format(self.elo)
        else:
            return self.elo

    def GetLiveElo(self, strng=False):
        """returns 'live' elo."""
        if strng:
            return "{0:.1f}".format(self.live_elo)
        else:
            return self.live_elo

    def GetPlayStrength(self):
        return self.play_strength.GetPlayStrength()

    def NameLength(self):
        """returns length of string returned by InvertName()."""
        return len(self.InvertName())

    def InvertName(self):
        """returns player's full name in "last, first" form."""
        name = self.last_name + ", " + self.first_name
        return name

    # Maintenance Functions
    def MonthlyMaintenance(self):
        self.UpdateElo()

    def WeeklyMaintenance(self):
        pass

    def DailyMaintenance(self):
        # self.ProcessTournamentInvites()
        self.pth.TransferToOld()
        self.pth.TransferToCurrent()

    def SetFederation(self, chess_federation):
        self.chess_federation = chess_federation

    def ProcessTournamentInvites(self):
        for invite in self.tournament_invites[:]:
            if self.EvaluateInvite(invite.GetInviter()):
                invite.Accept()
            else:
                invite.Decline()
                self.tournament_invites.remove(invite)

    def CancelTournament(self, t):
        self.pth.CancelTournament(t)

    def AddGame(self, game):
        if game not in self.pth.GetGameList():
            self.pth.AddGame(game)

    def AcceptCleanUp(self, inv):
        """
        overwrite this function from invitereceiver to add tournaments to list.
        """
        self.pth.AddNewTournament(inv.sender)

    def AddTournamentInvite(self, invite):
        self.tournament_invites.append(invite)

    def UpdateElo(self):
        self.elo = self.live_elo
        self.UpdateRow("elo", self.GetElo(strng=True))

    def UpdateLiveElo(self, rating_adjustment):
        self.live_elo += rating_adjustment
        self.UpdateRow("live_elo", self.GetLiveElo(strng=True))

    def EvaluateInvite(self, inv):
        """
        Evaluates an invitation from a tournament. Accepts or rejects the
        invite. If the player accepts the invite, adds the tournament to
        the player's tournament list.
        """
        if not self.pth.TournamentConflicts(inv.sender):
            return invitereceiver.invitereceiver.EvaluateInvite(self, inv)
        else:
            return 0

#    def RegisterForTournaments(self, tournaments):
#        """Takes a list of tournaments and chooses which of them to register for"""
#
#        #Basic Implementation
#        for t in tournaments:
#            if t.IsOpen():
#                if not self.pth.TournamentConflicts(t):
#                    t.AddPlayer(self)
