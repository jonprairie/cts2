from pydoc import locate


def LoadApplicationPackages(api, app_pkg_addressess):
    ret_dict = dict()
    for p in app_pkg_addressess:
        ret_dict.update(LoadPackage(api, p))
    return ret_dict


def LoadPackage(api, pkg):
    l = pkg.split(".")
    print "loading: " + pkg.split(".")[len(l)-1] + ", exposing:"
    handler = InitPackage(api, pkg)
    ret_dict = dict()
    for c in handler.expose:
        print "    " + c
        ret_dict.update(
            dict(
                (api_call, handler) for api_call in handler.expose
            )
        )
    return ret_dict


def InitPackage(api, pkg):
    return locate(pkg)(api)
