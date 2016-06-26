import tournament
import invitesender

class invitationaltournament(
    tournament.tournament,
    invitesender.invitesender
):

    def __init__(
        self,
        name,
        start_julian_date,
        num_player_range
    ):

        invitesender.invitesender.__init__(
            self,
            num_player_range
        )
        tournament.tournament.__init__(
            self,
            name,
            start_julian_date,
            num_player_range
        )
