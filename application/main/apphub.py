from pydoc import locate
import pkgloader
import api


class apphub:
    def __init__(self, app_pkg_addr):
        '''app container, loads packages/modules,
        builds the api, resolves dependencies and activates
        the packages/modules'''
        self.app_api = api.api()
        self.app_api.Update(
            pkgloader.LoadApplicationPackages(
                self.app_api,
                app_pkg_addr
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
