import screen as screen
import widget.scrollablelist as scrollablelist
import widget.selectablelist as selectablelist


class dynamicmenuscreen:
    # TODO: make key_dict/page_sz a default option
    # TODO: implement screen

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
            key_dict.update((x, self.Exit))
        self.list_widget = scrollablelist.scrollablelist(
            disp_list,
            key_dict,
            page_sz
        )
        self.view_list = selectablelist.selectablelist(
            self.list_widget.GetCurrentPage()
        )
        self.name = name
        self.exit = False
        self.display_only = False

    def __str__(self):
        return self.name.upper() + '\n' + str(self.view_list)

    def PassInput(self, inp):
        if inp in self.list_widget.key_dict.keys():
            temp = self.list_widget.key_dict[inp]()
            if temp:
                self.view_list.UpdateList(temp)
            return False
        elif inp in self.view_list.keys():
            _, chosen_element = self.view_list.GetElement(inp)
            self.menu_dict[chosen_element]()

    def PageUp(self):
        return self.list_widget.GetPrevPage()

    def PageDown(self):
        return self.list_widget.GetNextPage()

    def Exit(self):
        self.exit = True

    def GetExit(self):
        return self.exit
