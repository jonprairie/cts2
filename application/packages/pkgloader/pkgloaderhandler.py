from pydoc import locate
import packagelisting as pl
import cts2.application.util.pkg as pkg


class pkgloaderhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "pkg_loader",
            ["load_packages"],
            []
        )

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
        ret_dict = dict()
        for p in py_pkg_addrs:
            ret_dict.update(self.LoadPackage(p))
        return ret_dict

    def LoadPackage(self, pkg):
        l = pkg.split(".")
        print "loading: " + pkg.split(".")[len(l)-1] + ", exposing:"
        handler = self.InitPackage(pkg)
        ret_dict = dict()
        for c in handler.expose:
            print "    " + c
            ret_dict.update(
                dict(
                    (api_call, handler) for api_call in handler.expose
                )
            )
        return ret_dict

    def InitPackage(self, pkg):
        return locate(pkg)(self.api)
