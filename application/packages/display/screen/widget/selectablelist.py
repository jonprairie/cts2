class selectablelist:
    def __init__(self, l):
        self.key_list = "asfgqwrtzcvbhy123456nju7mki8lo9p0"
        self.s_list, self.s_dict = self.BuildList(l)

    def __str__(self):
        if self.s_list:
            ret_str = [
                str(t[0]) + "  ---  " + str(t[1]) for t in self.s_list
            ]
            ret_str[0] = ' ' + ret_str[0]
            return '\n '.join(ret_str)
        else:
            return ""

    def keys(self):
        return self.s_dict.keys()

    def GetElement(self, key):
        if key in self.s_dict.keys():
            return True, self.s_dict[key]
        else:
            return False, None

    def BuildList(self, s_list):
        dict_list = [
            (self.key_list[k], el) for k, el in enumerate(s_list)
        ]
        return dict_list, dict(dict_list)

    def UpdateList(self, l):
        self.s_list, self.s_dict = self.BuildList(l)
