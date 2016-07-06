import cts2.application.util.pkg as pkg
import logging
import os


class loghandler(pkg.pkg):
    def __init__(self, api):

        pkg.pkg.__init__(
            self,
            api,
            "log_handler",
            ["log_msg"],
            []
        )

        log_file = 'C:\Python27\Lib\site-packages\cts2\cts2.log'
        os.remove(log_file)

        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG
        )

        self.LogMsg("started", caller=self)

    def LogMsg(self, msg, lvl="info", caller=None):
        log_lvl = self.StrToConstant(lvl)
        if caller is not None:
            msg = self.StripCaller(caller) + ": " + msg
        msg += '\n'
        logging.log(log_lvl, msg)

    def StrToConstant(self, str):
        ret_const = None
        if str == "dbug":
            ret_const = logging.DEBUG
        elif str == "info":
            ret_const = logging.INFO
        elif str == "warn":
            ret_const = logging.WARNING
        elif str == "err":
            ret_const = logging.ERROR
        elif str == "crit":
            ret_const = logging.CRITICAL
        return ret_const

    def StripCaller(self, caller):
        return str(caller).split(".")[str(caller).count(".")][0:-1]
