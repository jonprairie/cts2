class pkg:
    def __init__(self, api, name, expose, dependencies):
        self.api = api
        self.name = name
        self.expose = expose
        self.dependencies = dependencies

    def Activate(self):
        pass
