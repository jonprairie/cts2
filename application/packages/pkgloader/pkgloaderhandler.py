from pydoc import locate
import packagelisting as pl
import cts2.util.pkg as pkg


class pkgloaderhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "pkg_loader",
            [
                "load_packages",
                "set_packages",
                "get_packages",
                "update_api_from_list"
            ],
            []
        )
        self.pkg_list = []

    def SetPackages(self, pkg_list):
        self.pkg_list = pkg_list

    def GetPackages(self):
        return self.pkg_list

    def DiscoverPackages(self, pkg_addr):
        py_pkg_addr = pkg_addr.replace("/", ".")
        return [
            ".".join(
                [
                    py_pkg_addr,
                    pkg,
                    pkg + "handler",
                    pkg + "handler"
                ]
            ) for pkg in pl.ListPackages(
                pkg_addr
            )
        ]

    def LoadPackages(self, pkg_addr):
        py_pkg_addrs = self.DiscoverPackages(pkg_addr)
        pkg_list = [self.LoadPackage(p) for p in py_pkg_addrs]
        self.api.Update(self.BuildExposeMappingFromList(pkg_list))
        return pkg_list

    def LoadPackage(self, pkg):
        l = pkg.split(".")
        print "loading: " + pkg.split(".")[-1] + ", exposing:"
        handler = self.InitPackage(pkg)
        self.pkg_list.append(handler)
        return handler

    def UpdateApiFromList(self, pkg_list):
        call_mapping = self.BuildExposeMappingFromList(pkg_list)
        self.api.Update(call_mapping)

    def BuildExposeMappingFromList(self, handlers):
        call_mapping = dict()
        for h in handlers:
            call_mapping.update(self.BuildExposeMapping(h))
        return call_mapping

    def BuildExposeMapping(self, handler):
        call_mapping = dict()
        for c in handler.expose:
            print "    " + c
            call_mapping.update(
                dict(
                    (api_call, handler) for api_call in handler.expose
                )
            )
        return call_mapping

    def InitPackage(self, pkg):
        return locate(pkg)(self.api)
