"""
representation of a screen.

a screen has two primary responsibilities:
1. to stringify itself
2. to receive input
"""


class screen:
    def __init__(self, name, widget_list=[]):
        self.name = name
        self.widget_list = widget_list
        self.key_dict = None
        self.exit = False

    def __str__(self):
        return self.ToString()

    def MakeExit(self):
        self.exit = True

    def GetExit(self):
        return self.exit

    def AddKeyDict(self, kd):
        self.key_dict = kd

    def PassInput(self, inp):
        if inp in self.key_dict:
            self.key_dict[inp]()
        else:
            for w in self.widget_list:
                if w.ProcessesInput(inp):
                    w.ProcessInput(inp)
                    break

    def ToString(self):
        return self.name + "\n\n" + "\n\n".join(
            [w.ToString() for w in self.widget_list]
        )
