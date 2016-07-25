"""
displays a non-interactive text message
"""
import widget


class popupmsg(widget.widget):
    def __init__(self, msg, name=""):
        self.msg = msg
        widget.widget.__init__(self, name)

    def ToString(self):
        if self.name:
            return str(self.name) + "\n" + str(self.msg)
        else:
            return str(self.msg)
