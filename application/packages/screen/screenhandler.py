"""
interface for creating screens
"""
import collections
import cts2.util.pkg as pkg
import screens.screen as screen
import widgets.popupmsg as popupmsg
import widgets.popupmsglist as popupmsglist
import widgets.scrollablelist as scrollablelist
import widgets.searchcontainer as searchcontainer
import widgets.sidescrollwidget as sidescrollwidget


class screenhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "screen_handler",
            [
                "build_tournament_screen",
                "build_search_player_screen",
                "build_tournament_search_screen"
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
        if t.finished:
            t_desc += ("\nchampion: " + t.GetChampion().InvertName())
        t_desc_w = popupmsg.popupmsg(t_desc)
        if t.started:
            # t_sch_w = scrollablelist.scrollablelist(
            #     "schedule:",
            #     t.schedule,
            #     page_size=1
            # )
            t_stand_w = popupmsg.popupmsg(t.GetStandings().ToString())
            ssw = sidescrollwidget.sidescrollwidget([
                t_desc_w, t_stand_w, player_list_w
            ])
        else:
            ssw = sidescrollwidget.sidescrollwidget([
                t_desc_w, player_list_w
            ])
        scr = screen.screen(
            "Tournament Display",
            [ssw]
        )
        scr.AddKeyDict(dict([("x", scr.MakeExit)]))
        return scr

    def BuildSearchPlayerScreen(
        self, player_list, send_player_screen
    ):
        sc_w = searchcontainer.searchcontainer(
            "player", player_list, send_player_screen
        )
        scr = screen.screen(
            "Search Player List",
            [sc_w]
        )
        scr.AddKeyDict(dict([("x", scr.MakeExit)]))
        return scr

    def BuildTournamentSearchScreen(
        self, tournament_list, send_tournament_screen
    ):
        sc_w = searchcontainer.searchcontainer(
            "tournament", tournament_list,
            send_tournament_screen
        )
        scr = screen.screen(
            "Search Tournament List",
            [sc_w]
        )
        scr.AddKeyDict(dict([("x", scr.MakeExit)]))
        return scr
