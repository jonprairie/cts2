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
        self.api.Update(
            self.api.Call(
                "load_packages",
                'cts2/game_instance'
            )
        )
        self.api.Call(
            "activate_packages",
            self.api.GetPackages()
        )
        self.game_instance_menu = gameinstancemenu.gameinstancemenu(
            self.api
        )
        self.api.Call(
            "add_screen",
            self.game_instance_menu.menu_screen
        )

    def LoadGame(self):
        '''TODO: Load game'''
        pass
