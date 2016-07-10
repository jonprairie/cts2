import cts2.application.packages.pkgloader.pkgloaderhandler as pl
import api


class apphub:
    def __init__(self, pkg_addr):
        '''app container, loads packages/modules,
        builds the api, resolves dependencies and activates
        the packages/modules'''
        self.app_api = api.api()

        # creates a pkgloader instance to load the initial packages.
        # this instance will load another instance into the api in
        # order to expose package-loading functionality.
        pkgl = pl.pkgloaderhandler(self.app_api)
        self.app_api.Update(
            pkgl.LoadPackages(
                pkg_addr
            )
        )
        self.app_api.Call(
            "activate_packages",
            self.app_api.GetPackages()
        )

    def GameLoop(self):
        self.app_api.Call("display")
        inp = self.app_api.Call("read_sysin")
        inp_msg = "passing input: " + inp + " to screen: " + str(self.app_api.Call("get_top_screen"))
        self.app_api.Call("log_msg", inp_msg)
        self.app_api.Call("get_top_screen").PassInput(inp)
