from pydoc import locate
import api


class apphub:
    def __init__(self, application_package_addresses):
        '''app container, loads packages/modules,
        builds the api, resolves dependencies and activates
        the packages/modules'''
        self.app_api = api.api(
            self.LoadApplicationPackages(
                application_package_addresses
            )
        )
        self.ActivateApplicationPackages()

    def LoadApplicationPackages(self, app_pkg_addressess):
        '''To add a package, insert an entry into this list. The
        entry should be the python path to the class that exposes
        that package's api. The __init__ method of this class
        should not rely on resources external to the package, but
        should instead create two lists of strings. One representing
        the api calls that the class exposes (called api_expose),
        the other representing the external api-call dependencies to
        activate the class (called api_init_dependencies). The package
        loader will then call the Activate method on that class later
        to allow any necessary, external api calls.'''
        ret_dict = dict()
        for p in app_pkg_addressess:
            handler = self.InitPackage(p)
            ret_dict.update(
                dict(
                    (api_call, handler) for api_call in handler.expose
                )
            )
        return ret_dict

    def InitPackage(self, pkg):
        print "loading: " + pkg
        try:
            p = locate(pkg)()
        except:
            raise
        print "loaded:  " + pkg
        return p

    def ActivateApplicationPackages(self):
        pass

    def GameLoop(self):
        raise Exception('exit')
