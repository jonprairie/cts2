import cts2.application.util.pkg as pkg


class pkgactivatorhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "package_activator_handler",
            ["activate_packages"],
            []
        )
        self.activated_ledger = dict()
        self.dep_web = dict()

    def UpdatePackageInfo(self, pkgs):
        self.activated_ledger.update(
            dict(
                (pkg.name, False) for pkg in pkgs
                if pkg.name not in self.activated_ledger
            )
        )
        self.dep_web.update(
            dict(
                (api_call, pkg) for pkg in pkgs
                for api_call in pkg.expose
            )
        )

    def ActivatePackages(self, pkgs):
        self.UpdatePackageInfo(pkgs)
        ancestors = []
        for pkg in pkgs:
            try:
                self.ActivatePkg(pkg, ancestors)
            except:
                raise

    def ActivatePkg(self, pkg, ancestors):
        if not self.activated_ledger[pkg.name]:
            if pkg not in ancestors:
                ancestors.append(pkg)
                for p in [
                    self.dep_web[d] for d in pkg.dependencies
                ]:
                    self.ActivatePkg(p, ancestors)
                print "activating: ", pkg.name
                pkg.Activate()
                self.activated_ledger[pkg.name] = True
                ancestors.remove(pkg)
            else:
                raise Exception(
                    'cycle detected in package activation: ' +
                    " ==> ".join([a.name for a in ancestors])
                )
