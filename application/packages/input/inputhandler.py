import cts2.application.util.pkg as pkg


class inputhandler(pkg.pkg):
    def __init__(self, api):
        # TODO: change cursor to a default option
        pkg.pkg.__init__(
            self,
            api,
            "input_handler",
            ["read_sysin"],
            ["log_msg"]
        )

    def ReadSysin(self, cursor="\n--> "):
        return raw_input(cursor)
