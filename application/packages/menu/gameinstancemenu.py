import cts2.application.util.stringtable as stringtable
import cts2.application.packages.menu.arch.node as node
import cts2.application.packages.menu.arch.menudriver as menudriver
import cts2.application.packages.display.screen.dynamicmenuscreen as dms


class gameinstancemenu:
    def __init__(self, api):
        self.menu_screen, self.tourn_scr = self.BuildMenu()
        self.api = api

        self.exit_question = event.displayyesornomessage(
            "Are you sure that you want to exit?"
        )
        # self.disp_menu_frame = event.displayinputmessage(
        #   self.menu_driver.GetStringTable()
        # )
        self.get_player_list = getplayerlist.getplayerlist()
        self.get_future_tournaments = messageevent.messageevent(
            "get_non_started_tournament_list"
        )
        self.get_current_tournaments = messageevent.messageevent(
            "get_current_tournament_list"
        )
        self.advance_day = messageevent.messageevent("advance_day")
        self.advance_day.num_days = 1
        self.display_string = messageevent.messageevent(
            "display_string"
        )
        self.display_screen = messageevent.messageevent(
            "display_screen"
        )
        self.display_string_table = event.displaystringtable(
            [],
            header="Top 10 Players (World)",
            line_num=10
        )

        self.exit = False

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

    def MenuFrame(self):
        self.disp_menu_frame = event.displayinputmessage(
            self.menu_driver.GetStringTable()
        )
        self.event_handler.ProcessEvent(self.disp_menu_frame)
        self.menu_driver.Select(self.disp_menu_frame.response)

    def AdvanceDay(self):
        self.event_handler.ProcessEvent(self.advance_day)

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
        self.event_handler.ProcessEvent(
            self.get_current_tournaments
        )
        tournament_screen = menuscreen.menuscreen(
            "current_current_tournament_list",
            self.get_current_tournaments.tournament_list,
            self.DisplayTournament
        )
        self.display_screen.screen = tournament_screen
        self.event_handler.ProcessEvent(self.display_screen)

    def FutureTournaments(self):
        self.event_handler.ProcessEvent(self.get_future_tournaments)
        # self.event_handler.ProcessEvent(self.get_current_tournaments)
        future_tourn_st = stringtable.stringtable(
            "Upcoming Tournaments",
            self.get_future_tournaments.tournament_list
        )
        self.display_string_table.st = future_tourn_st
        self.event_handler.ProcessEvent(self.display_string_table)

    def DisplayTournament(self, t):
        self.display_string.st = "\n".join(
            [
                "tournament: " + t.name,
                "starts: " + str(t.start_julian_date),
                "player list:\n" + "\n".join(
                    [str(p) for p in t.player_list]
                )
            ]
        )
        self.event_handler.ProcessEvent(self.display_string)

    def Calendar(self):
        print "this is the calendar\n\tisn't it beautiful?"

    def MakeExit(self):
        self.event_handler.ProcessEvent(self.exit_question)
        if self.exit_question.response == "yes":
            self.exit = True
