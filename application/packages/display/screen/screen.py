class screen:
    def __init__(self, key_dict, header=""):
        '''TODO: add support for multiple widgets'''
        self.key_dict = key_dict
        self.exit = False

    def PassInput(self, input):
        if input in self.key_dict.keys():
            self.key_dict[input]()
        else:
            pass

    def MakeExit(self):
        self.exit = True

    def GetExit(self):
        return self.exit

    def __str__(self):
        return header or str(self)
