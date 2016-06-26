import cts2.game_instance.tournament.invitationaltournament as invitationaltournament
import cts2.game_instance.tournament.doubleroundrobin as doubleroundrobin

class drrinvitational(
    invitationaltournament.invitationaltournament,
    doubleroundrobin.doubleroundrobin
):

    def __init__(
        self,
        name,
        start_julian_date,
        num_player_range
    ):
        """double round robin, invitational tournament"""

        invitationaltournament.invitationaltournament.__init__(
            self,
            name,
            start_julian_date,
            num_player_range
        )
        doubleroundrobin.doubleroundrobin.__init__(
            self
        )
