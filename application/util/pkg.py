class pkg:
    def __init__(
        self,
        api,
        name,
        expose,
        dependencies,
        save_ind=False
    ):
        '''pkg should set save_ind if pkg should be saved
        on save game'''
        self.api = api
        self.name = name
        self.expose = expose
        self.dependencies = dependencies
        self.save_ind = save_ind

    def Activate(self):
        pass

    def RemoveAPI(self):
        self.api = None

    def AddAPI(self, api):
        self.api = api

    def GetExposeMapping(self):
        return dict((e, self) for e in self.expose)
