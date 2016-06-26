import cts2.application.util.eventprocessor as eventprocessor


class inputhandler(eventprocessor.eventprocessor):
    def __init__(self, event_handler):
        # TODO: change cursor to a default option

        # initialize module as an eventprocessor
        self.event_dict = dict(
            read_sysin=self.ReadSysin
        )
        eventprocessor.eventprocessor.__init__(
            self,
            self.event_dict,
            event_handler
        )

    def ReadSysin(self, ev):
        ev.input = raw_input("\n--> ")
