"""
displays a non-interactive text message from a list of
stringable objects.
"""
import popupmsg


class popupmsglist(popupmsg.popupmsg):
    def __init__(self, msglist, name="", seperator="\n"):
        popupmsg.popupmsg.__init__(
            self,
            seperator.join([str(m) for m in msglist]),
            name
        )
