"""
game instance menu
"""
import cts2.util.stringtable as stringtable
import cts2.application.packages.menu.arch.node as node
import cts2.application.packages.menu.arch.menudriver as menudriver
import cts2.application.packages.display.screen.dynamicmenuscreen as dms
import cts2.application.packages.display.screen.areyousure as ays
import cts2.application.packages.display.screen.popup as popup
import cts2.application.packages.display.screen.listmenu as listmenu
import collections
import pdb


class gameinstancemenu:
    def __init__(self, api):
        self.menu_screen, self.tourn_scr, self.player_scr = self.BuildMenu()
        self.api = api

    def BuildMenu(self):
        temp_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Game Menu",
            dict([
                ("advance day", self.AdvanceDay),
                ("calendar", self.Calendar),
                ("players", self.SendPlayerScreenTopLevel),
                ("tournaments", self.SendTournamentScreen),
                ("save game", self.SaveGame),
                ("exit", self.MakeExit),
                ("debug", self.Debug)
            ]),
            add_exit=False
        )
        tourn_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Tournaments",
            dict([
                ("current tournaments", self.CurrentTournaments),
                ("future tournaments", self.FutureTournaments),
                ("finished tournaments", self.FinishedTournaments),
                ("search tournaments", self.SendTournamentSearchScreen)
            ])
        )
        player_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Players",
            dict([
                ("top players", self.TopPlayers),
                ("search players", self.SendPlayerSearchScreen),
                ("player list", self.SendPlayerScreen)
            ])
        )
        return temp_scr, tourn_scr, player_scr

    def AdvanceDay(self):
        self.api.Call("advance_day")

    def SendPlayerScreenTopLevel(self):
        self.api.Call("add_screen", self.player_scr)

    def TopPlayers(self):
        player_list = self.api.Call(
            "get_top_players_by_elo", 10
        )
        player_st = stringtable.stringtable(
            "Players",
            player_list
        )
        self.api.Call(
            "add_screen",
            popup.popup(player_st.ToString(row_num=10))
        )

    def SendPlayerSearchScreen(self):
        player_list = self.api.Call("get_player_list")
        scr = self.api.Call(
            "build_search_player_screen",
            player_list,
            self.DisplayPlayer
        )
        self.api.Call("add_screen", scr)

    def SendPlayerScreen(self):
        player_list = self.api.Call("get_player_list")
        player_scr = listmenu.listmenu(
            "players",
            player_list,
            self.DisplayPlayer
        )
        self.api.Call("add_screen", player_scr)

    def DisplayPlayer(self, p):
        strg = "\n".join(
            [
                "player: " + p.InvertName(),
                "age: " + str(p.age),
                "elo: " + p.GetElo(True),
                "live elo: " + p.GetLiveElo(True),
                "curr tourn: " + str(p.pth.GetCurrentTournament()),
                "\ngames:\n" + "\n".join(
                    [str(g) for g in p.pth.GetGameList()]
                ),
                "\ntournaments:\n" + "\n".join(
                    [
                        str(t) + " " + str(t.start_julian_date)
                        for t in p.pth.GetFutureTournaments()
                    ]
                )
            ]
        )
        self.api.Call("add_screen", popup.popup(strg))

    def SendTournamentScreen(self):
        self.api.Call("add_screen", self.tourn_scr)

    def SendTournamentSearchScreen(self):
        tournament_list = self.api.Call("get_tournament_list")
        scr = self.api.Call(
            "build_tournament_search_screen",
            tournament_list,
            self.DisplayTournament
        )
        self.api.Call("add_screen", scr)

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

    def FinishedTournaments(self):
        fin_tournament_list = self.api.Call(
            "get_finished_tournaments"
        )
        tournament_screen = listmenu.listmenu(
            "finished tournaments",
            fin_tournament_list,
            self.DisplayTournament
        )
        self.api.Call("add_screen", tournament_screen)

    def DisplayTournament(self, t):
        self.api.Call(
            "add_screen",
            self.api.Call("build_tournament_screen", t)
        )

    def Calendar(self):
        today = self.api.Call("get_current_julian")
        self.api.Call(
            "add_screen",
            popup.popup("today is: " + str(today))
        )

    def SaveGame(self):
        self.api.Call("save_game")

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

    def Debug(self):
        pdb.set_trace()

    def FindTournamentConflicts(self):
        # useful for verifying that players aren't double-booking
        # tournaments
        player_list = self.api.Call("get_player_list")
        ret_cnt_list = []
        for player in player_list:
            cnt = collections.Counter()
            for tournament in player.pth.GetFutureTournaments():
                for date in tournament.GetDateRange():
                    cnt[date] += 1
            ret_cnt_list.append((player.last_name+", "+player.first_name, cnt))
        flat_tc = [(p,d,n) for (p,t) in ret_cnt_list for (d,n) in t.items()]
        tc_error = [x for x in flat_tc if x[2] > 1]
        return ret_cnt_list, tc_error

