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

    def BuildMenu(self):
        temp_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Game Menu",
            dict([
                ("advance day", self.AdvanceDay),
                ("calendar", self.Calendar),
                ("top players", self.TopPlayers),
                ("tournaments", self.SendTournamentScreen),
                ("save game", self.SaveGame),
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
        self.player_list = self.api.Call(
            "get_player_list"
        )
        player_st = stringtable.stringtable(
            "Players",
            self.player_list
        )
        player_st.SortBy("elo", ascending=False)
        self.api.Call(
            "add_screen",
            popup.popup(player_st.ToString(row_num=10))
        )

    def CurrentTournaments(self):
        tournament_list = self.api.Call(
            "get_current_tournaments"
        )
        tournament_screen = listmenu.listmenu(
            "current tournaments",
            tournament_list,
            self.DisplayTournament
        )
        self.api.Call("add_screen", tournament_screen)

    def FutureTournaments(self):
        fut_tournament_list = self.api.Call(
            "get_future_tournaments"
        )
        tournament_screen = listmenu.listmenu(
            "future tournaments",
            fut_tournament_list,
            self.DisplayTournament
        )
        self.api.Call("add_screen", tournament_screen)

    def DisplayTournament(self, t):
        '''TODO: add dedicated tournament display scree'''
        strg = "\n".join(
            [
                "tournament: " + t.name,
                "starts: " + str(t.start_julian_date),
                "player list:\n" + "\n".join(
                    [str(p) for p in t.player_list]
                )
            ]
        )
        self.api.Call("add_screen", popup.popup(strg))

    def Calendar(self):
        print "this is the calendar\n\tisn't it beautiful?"

    def SaveGame(self):
        self.api.Call("save_game")
        # self.api.Call(
        #     "add_screen",
        #     popup.popup(
        #         str(
        #             self.api.GetSavePackages()
        #         )
        #     )
        # )

    def MakeExit(self):
        self.last_chance = ays.areyousure(
            self.TrueExit,
            " that you want to exit"
        )
        self.api.Call("add_screen", self.last_chance)

    def TrueExit(self):
        '''TODO: Save game on exit'''
        self.last_chance.MakeExit()
        self.menu_screen.MakeExit()
