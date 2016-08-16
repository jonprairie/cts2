class country:
    def __init__(
        self, iso, iso3, fips, name, capital,
        population, continent, languages, neighbors
    ):
        self.iso = str(iso)
        self.iso3 = str(iso3)
        self.fips = str(fips)
        self.name = str(name)
        self.capital = str(capital)
        self.population = str(population)
        self.continent = str(continent)
        self.languages = str(languages)
        self.neighbors = str(neighbors)

    def GetName(self):
        return self.name

    def GetShortName(self):
        return self.iso3

# russia = country("russia", "rus", "russian")
# usa = country("usa", "usa", "american")
# germany = country("germany", "ger", "german")
# france = country("france", "fra", "french")
# norway = country("norway", "nor", "norwegian")
# armenia = country("armenia", "arm", "armenian")
# ukraine = country("ukraine", "ukr", "ukranian")
# china = country("china", "chi", "chinese")
# india = country("india", "ind", "indian")
# spain = country("spain", "spa", "spanish")
# england = country("england", "eng", "english")
# japan = country("japan", "jap", "japanese")
# world = country("terra", "ter", "terran")
# country_list = ([
#     russia, usa, germany,france,
#     norway, armenia, ukraine,
#     china, india, spain, england, japan
# ])
