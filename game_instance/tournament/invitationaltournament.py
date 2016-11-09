import cts2.util.comm.invitesender as invitesender
import tournament

class invitationaltournament:
    def __init__(
            self,
            name,
            start_julian_date,
            num_player_range,
            schedule
    ):

        self.invite_sender = invitesender.invitesender(
            num_player_range
        )
        self.tournament = tournament.tournament(
            name,
            start_julian_date,
            num_player_range,
            schedule
        )
