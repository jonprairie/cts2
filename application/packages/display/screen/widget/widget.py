class widget:
    def __init__(self, key_dict):
        self.key_dict = key_dict

    def PassInput(self, input):
        if input in self.key_dict.keys():
            return self.key_dict[input]()
