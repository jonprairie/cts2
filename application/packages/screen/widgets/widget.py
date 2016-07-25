"""
representation of a widget.
"""


class widget:
    def __init__(self, name=""):
        self.name = name
        self.key_dict = None

    def AddKeyDict(self, kd):
        self.key_dict = kd

    def ProcessesInput(self, inp):
        if inp in self.key_dict:
            return True
        else:
            return False

    def ProcessInput(self, inp):
        self.key_dict[inp]()

    def ToString(self):
        return str(self.name)
