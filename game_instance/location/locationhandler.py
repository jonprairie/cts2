"""
handles interfacing to various location services
"""
import sqlite3
import random
import cts2.util.pkg as pkg
import country


class locationhandler(pkg.pkg):
    def __init__(self, api):
        pkg.pkg.__init__(
            self,
            api,
            "location_handler",
            [
                "get_random_city",
                "get_country_list"
            ],
            ["log_msg"]
        )

    def Activate(self):
        self.conn = sqlite3.connect('../../database/countries/ctry.db')
        self.curs = self.conn.cursor()

        if self.conn:
            self.api.Call("log_msg", "loaded location database connection")
        else:
            raise Exception("location database could not be loaded")

        self.country_dict = self.BuildCountryDict()
        self.cities_dict = self.BuildCitiesDict()

        for i in self.cities_dict.keys():
            if not self.cities_dict[i]:
                del self.country_dict[i]
                del self.cities_dict[i]

    def GetRandomCity(self, country=None):
        if country is not None:
            country_key = country.iso
        else:
            country_key = random.choice(self.country_dict.keys())

        search_str = (
            "select asciiname from city_list where geonameid=?;"
        )

        try:
            results = list(
                self.curs.execute(
                    search_str,
                    [random.choice(self.cities_dict[country_key])]
                )
            )
            return str(results[0][0])
        except IndexError:
            import pdb; pdb.set_trace()

    def GetCountryList(self):
        return self.country_dict.values()

    def BuildCountryDict(self):
        search_str = (
            "select iso, iso3, fips, country, capital, " +
            "population, continent, languages, neighbors " +
            "from ctry;"
        )
        results = list(self.curs.execute(search_str))
        return dict(
            (r[0], country.country(*r)) for r in results
        )

    def BuildCitiesDict(self):
        search_str = (
            "select geonameid from city_list where " +
            "ccode = ?;"
        )
        return dict(
                (
                    c.iso,
                    [x[0] for x in list(
                        self.curs.execute(
                            search_str, [c.iso]
                        )
                    )]
                )
                for c in self.country_dict.values()
            )
