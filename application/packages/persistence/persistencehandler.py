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
        self.api.Update(
            self.api.Call(
                "load_packages",
                'cts2/game_instance'
            )
        )
        full_path = self.default_options["save_game_path"] + "save.cts"
        with open(full_path, "r") as save_file:
            save_list = cPickle.load(save_file)
        pkg_list = self.api.GetPackages()
        current_keys = [
            k for pckg in self.api.GetSavePackages() for k in pckg.expose
        ]
        save_keys = [k for handler in save_list for k in handler.expose]
        key_int = set(save_keys) & set(current_keys)
        for k in save_keys + current_keys:
            if k not in key_int:
                raise Exception("version not compatible, key: " + str(k))
        new_expose_dict = dict()
        for d in [
            handler.GetExposeMapping() for handler in save_list
        ]:
            new_expose_dict.update(d)
        self.api.Update(new_expose_dict)
