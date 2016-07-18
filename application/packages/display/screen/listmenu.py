import dynamicmenuscreen


class listmenu(dynamicmenuscreen.dynamicmenuscreen):
    def __init__(self, name, disp_list, func, *args, **kwargs):
        self.name = name
        self.func = func
        menu_dict = dict((d, func) for d in disp_list)
        dynamicmenuscreen.dynamicmenuscreen.__init__(
            self,
            name,
            menu_dict,
            *args,
            **kwargs
        )

    def PassToInternal(self, inp):
        _, chosen_element = self.slct_list.GetElement(inp)
        self.func(chosen_element)
