import screen as screen
import widget.scrollablelist as scrollablelist
import widget.selectablelist as selectablelist


class dynamicmenuscreen:
    # TODO: make key_dict/page_sz a default option
    # TODO: implement screen/refactor, screens should handle input, not widgets

    def __init__(
        self,
        name,
        menu_dict,
        page_sz=10,
        add_exit=True
    ):
        self.menu_dict = menu_dict
        disp_list = [k for k in self.menu_dict.keys()]
        key_dict = dict(
            e=self.PageUp,
            d=self.PageDown
        )
        if add_exit:
            key_dict.update([('x', self.MakeExit)])
        self.scroll_list = scrollablelist.scrollablelist(
            disp_list,
            key_dict,
            page_sz
        )
        self.slct_list = selectablelist.selectablelist(
            self.scroll_list.GetCurrentPage()
        )
        self.name = name
        self.exit = False
        self.display_only = False

    def __str__(self):
        return self.name.upper() + '\n' + str(self.slct_list)

    def PassInput(self, inp):
        if inp in self.scroll_list.key_dict.keys():
            return self.PassToList(inp)
        elif inp in self.slct_list.keys():
            self.PassToInternal(inp)

    def PassToList(self, inp):
        self.scroll_list.key_dict[inp]()
        temp = self.scroll_list.GetCurrentPage()
        if temp:
            self.slct_list.UpdateList(temp)
        return False

    def PassToInternal(self, inp):
        _, chosen_element = self.slct_list.GetElement(inp)
        self.menu_dict[chosen_element]()

    def PageUp(self):
        return self.scroll_list.GetPrevPage()

    def PageDown(self):
        return self.scroll_list.GetNextPage()

    def MakeExit(self):
        self.exit = True

    def GetExit(self):
        return self.exit
