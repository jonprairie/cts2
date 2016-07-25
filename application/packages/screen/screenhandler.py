"""
interface for creating screens
"""
import cts2.util.pkg as pkg
import screens.screen as screen
import widgets.popupmsg as popupmsg
import widgets.popupmsglist as popupmsglist
import widgets.sidescrollwidget as sidescrollwidget


class screenhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "screen_handler",
            [
                "build_tournament_screen"
            ],
            []
        )

    def BuildTournamentScreen(self, t):
        player_list_w = popupmsglist.popupmsglist(
            t.player_list,
            "tournament participants:"
        )
        t_desc = "\n".join([
            "tournament: " + t.name,
            "starts: " + str(t.start_julian_date)
        ])
        t_desc_w = popupmsg.popupmsg(t_desc)
        t_sch_w = popupmsglist.popupmsglist(
            t.schedule,
            "schedule:"
        )
        ssw = sidescrollwidget.sidescrollwidget([
            t_desc_w, player_list_w, t_sch_w
        ])
        scr = screen.screen(
            "Tournament Display",
            [ssw]
        )
        scr.AddKeyDict(dict([("x", scr.MakeExit)]))
        return scr
