import cts2.application.util.pkg as pkg
import arch.node as node
import arch.menudriver as menudriver
import cts2.application.packages.display.screen.areyousure as ays
import cts2.application.packages.display.screen.dynamicmenuscreen as dms
import gameinstancemenu as gameinstancemenu


class menuhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "menu_handler",
            ["menu_mux"],
            ["add_screen"]
        )

        self.menu_screen = self.BuildMainMenu()
        self.menu_stack = [self]

    def Activate(self):
        self.api.Call("add_screen", self.menu_screen)

    def BuildMainMenu(self):
        temp_scr = dms.dynamicmenuscreen(
            "Chess Tournament Sim - Main Menu",
            dict([
                ("new game", self.NewGame),
                ("load game", self.LoadGame),
                ("exit", self.MakeExit)
            ]),
            add_exit=False
        )
        return temp_scr

    def MakeExit(self):
        self.api.Call(
            "add_screen",
            ays.areyousure(
                self.RaiseExit,
                " that you want to exit"
            )
        )

    def RaiseExit(self):
        raise Exception('exit')

    def NewGame(self):
        # self.event_handler.ProcessEvent(self.init_game_instance_handlers)
        # temp_menu = gameinstancemenu.gameinstancemenu()
        # temp_menu.event_handler = self.event_handler
        # self.menu_stack.append(temp_menu)
        pass

    def LoadGame(self):
        pass
