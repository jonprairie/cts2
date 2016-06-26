import logging
import os

class loghandler:
    def __init__(self, event_handler):

        self.event_handler = event_handler
        self.event_dict = dict(
            log_message=self.LogMsg
        )

        log_file = 'C:\Python27\Lib\site-packages\cts2\cts2.log'
        os.remove(log_file)

        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG
        )

        logging.debug(self.StripSender(self) + ':\n\tstarted\n')

    def ProcessEvent(self, ev):
        try:
            self.event_dict[ev.event_type](ev)
        except:
            raise

    def LogMsg(self, ev):
        sender = self.StripSender(ev.sender)
        msg = sender + ':\n\t'
        msg += ev.message
        msg += '\n'
        logging.debug(msg)

    def StripSender(self, sender):
        s = str(sender).split(".")
        return  "<" + s[len(s)-1]
