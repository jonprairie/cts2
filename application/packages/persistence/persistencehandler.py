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
