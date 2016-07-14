import cts2.application.packages.pkgloader.pkgloaderhandler as pl
import api


class apphub:
    def __init__(self, pkg_addr):
        '''app container, loads packages/modules,
        builds the api, resolves dependencies and activates
        the packages/modules'''
        # TODO: implement pkgcontainer class, to persist pkgs?
        # Right now it's left to api, but that sort of violates SRP.
        # Pkgs that don't expose functionality have to expose "dummy"
        # functionality to "stay alive".
        self.app_api = api.api()

        # creates a pkgloader instance to load the initial packages.
        # this instance will load another pkgloader instance into the
        # api in order to expose package-loading functionality.
        pkgl = pl.pkgloaderhandler(self.app_api)
        pkg_list = pkgl.LoadPackages(pkg_addr)

        self.app_api.Call(
            "activate_packages",
            self.app_api.GetPackages()
        )

        self.app_api.Call("set_packages", pkg_list)

    def GameLoop(self):
        self.app_api.Call("display")
        inp = self.app_api.Call("read_sysin")
        inp_msg = "passing input: " + inp + " to screen: " + str(self.app_api.Call("get_top_screen"))
        self.app_api.Call("log_msg", inp_msg)
        self.app_api.Call("get_top_screen").PassInput(inp)
