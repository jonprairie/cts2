import cts2.application.events.getdefaultoptions as getdefaultoptions

class optionconsumer:
    def __init__(self):
        self.get_default_options = getdefaultoptions.getdefaultoptions()
        self.event_handler.ProcessEvent(self.get_default_options)
        self.default_options = self.get_default_options.option_dict
