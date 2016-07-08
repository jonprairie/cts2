import screen


class menuscreen(screen.screen):
    def __init__(self, menu_dict, header=""):
        self.menu_dict = menu_dict
        key_dict = {
            (k, menu_dict[k][1]) for k in menu_dict.keys()
        }
        screen.screen.__init__(key_dict, header)

    def __str__(self):
        pass
