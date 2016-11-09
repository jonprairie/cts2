import random


class federation:
    def __init__(self, api, country):
        self.api = api
        self.country = country

        self.td_list = []
        for i in range(random.randint(1, 4)):
            temp_td = api.Call("create_tournament_director", country)
            self.td_list.append(temp_td)
