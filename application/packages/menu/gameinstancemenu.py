import cts2.application.util.stringtable as stringtable
import cts2.application.packages.menu.arch.node as node
import cts2.application.packages.menu.arch.menudriver as menudriver
import cts2.application.packages.display.screen.dynamicmenuscreen as dms
import cts2.application.packages.display.screen.areyousure as ays
import cts2.application.packages.display.screen.popup as popup
import cts2.application.packages.display.screen.listmenu as listmenu

class gameinstancemenu:
    def __init__(self, api):
        self.menu_screen, self.tourn_scr = self.BuildMenu()
        self.api = api

        # self.display_string_table = event.displaystringtable(
        #     [],
        #     header="Top 10 Players (World)",
        #     line_num=10
        # )

    def BuildMenu(self):
        temp_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Game Menu",
            dict([
                ("advance day", self.AdvanceDay),
                ("calendar", self.Calendar),
                ("top players", self.TopPlayers),
                ("tournaments", self.SendTournamentScreen)
                ("exit", self.MakeExit)
            ]),
            add_exit=False
        )
        tourn_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Tournaments",
            dict([
                ("current tournaments", self.CurrentTournaments),
                ("future tournaments", self.FutureTournaments)
            ])
        )
        return temp_scr, tourn_scr

    def SendTournamentScreen(self):
        self.api.Call("add_screen", self.tourn_scr)

    def AdvanceDay(self):
        self.api.Call("advance_day")

    def TopPlayers(self):
        self.event_handler.ProcessEvent(self.get_player_list)
        player_st = stringtable.stringtable(
            "Players",
            self.get_player_list.player_list
        )
        player_st.SortBy("elo", ascending=False)
        self.display_string_table.st = player_st
        self.event_handler.ProcessEvent(self.display_string_table)

    def CurrentTournaments(self):
        self.tournament_list = self.api.Call(
            "get_current_tournament_list"
        )
        tournament_screen = listmenu.listmenu(
            self.tournament_list,
            self.DisplayTournament
        )
        self.api.Call("add_screen", self.tournament_screen)

    def FutureTournaments(self):
        self.fut_tournament_list = self.api.Call(
            "get_non_started_tournament_list"
        )
        tournament_screen = listmenu.listmenu(
            self.fut_tournament_list,
            self.DisplayTournament
        )
        self.api.Call("add_screen", self.tournament_screen)

    def DisplayTournament(self, t):
        str = "\n".join(
            [
                "tournament: " + t.name,
                "starts: " + str(t.start_julian_date),
                "player list:\n" + "\n".join(
                    [str(p) for p in t.player_list]
                )
            ]
        )
        self.api.Call(
            "add_screen",
            popup.popup(str)
        )

    def Calendar(self):
        print "this is the calendar\n\tisn't it beautiful?"

    def MakeExit(self):
        self.api.Call(
            "add_screen",
            ays.areyousure(
                self.menu_screen.MakeExit,
                " that you want to exit"
            )
        )
