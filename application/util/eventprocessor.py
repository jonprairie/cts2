import optionconsumer
import logger

class eventprocessor(
    optionconsumer.optionconsumer,
    logger.logger
):

    def __init__(self, event_dict, event_handler):
        self.event_handler = event_handler
        optionconsumer.optionconsumer.__init__(self)
        self.event_dict = event_dict
        logger.logger.__init__(self)

    def ProcessEvent(self, ev):
        try:
            self.event_dict[ev.event_type](ev)
        except:
            raise
            #raise Exception(ev.event_type + " is not a valid Event Type for " + str(self))
