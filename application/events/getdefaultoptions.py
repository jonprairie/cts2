import event

class getdefaultoptions(event.event):
    def __init__(self, option_keys=False):
        event.event.__init__(self, "get_default_options")
        self.option_keys = option_keys
        self.option_dict = False
