import cts2.application.util.pkg as pkg
import cPickle
import os


class persistencehandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "persistence_handler",
            [
                "save_game",
                "load_game"
            ],
            ["def_options"]
        )

    def Activate(self):
        self.default_options = self.api.Call(
            "def_options",
            ["save_game_path"]
        )

    def SaveGame(self):
        full_path = self.default_options["save_game_path"] + "save.cts"
        try:
            os.remove(full_path)
        except:
            pass
        save_list = self.api.GetSavePackages()
        for handler in save_list:
            handler.RemoveAPI()
        with open(full_path, "a+") as save_file:
            cPickle.dump(save_list, save_file)
        for handler in save_list:
            handler.AddAPI(self.api)

    def LoadGame(self):
        full_path = self.default_options["save_game_path"] + "save.cts"
        with open(full_path, "r") as save_file:
            save_list = cPickle.load(save_file)
        pkg_list = self.api.Call("get_packages")
        current_keys = set(
            k for pckg in self.api.GetSavePackages() for k in pckg.expose
        )
        save_keys = set(k for handler in save_list for k in handler.expose)
        key_diff = save_keys ^ current_keys
        if key_diff:
            raise Exception(
                "version not compatible, missing functionality: " + str(key_dif)
            )
        return save_list
