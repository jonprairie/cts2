"""
invitational match tournament between two players
"""
import cts2.game_instance.tournament.invitationaltournament as it
import cts2.game_instance.tournament.singlematch as singlematch


class matchinvitational(
    it.invitationaltournament,
    singlematch.singlematch
):

    def __init__(
        self,
        name,
        start_julian_date
    ):
        """double round robin, invitational tournament"""

        it.invitationaltournament.__init__(
            self,
            name,
            start_julian_date,
            (2, 2)
        )
        singlematch.singlematch.__init__(
            self
        )
