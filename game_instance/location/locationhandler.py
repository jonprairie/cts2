"""
handles interfacing to various location services
"""
import sqlite3
import cts2.util.pkg as pkg


class locationhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "location_handler",
            [
                "get_random_city",
                "get_random_country"
            ],
            ["log_msg"]
        )

    def Activate(self):
        self.conn = sqlite3.connect('../../database/ctry.db')
        self.curs = self.conn.cursor()
        if self.conn:
            self.api.Call("log_msg", "loaded database connection")

    def GetRandomCity(self, country=None):
        pre_string = "select * from cities"
        cond = ""
        post_string = "order by random() limit 1"
        if country is not None:
            cond = " where ccode = '" + country + "' "
        search_str = pre_string + cond + post_string
        return list(self.curs(search_str))[0]

    def GetRandomCountry(self):
        search_str = "select country from ctry order by random() limit 1"
        return list(self.curs(search_str))[0]
