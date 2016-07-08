import screen
import cts2.application.util.misc as misc


class areyousure(screen.screen):
    def __init__(self, callback, msg=""):
        self.msg = msg
        self.callback = callback
        screen.screen.__init__(
            self,
            misc.MultiDictInit(
                (['y', 'Y', 'yes', 'Yes'], self.callback),
                (['n', 'N', 'no', 'No'], self.MakeExit)
            )
        )

    def __str__(self):
        return "are you sure" + (self.msg and ("" + self.msg)) + "? "
