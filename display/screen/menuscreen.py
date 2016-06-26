import screen as screen
import widget.scrollablelist as scrollablelist
import widget.selectablelist as selectablelist


class menuscreen:
    # TODO: make key_dict/page_sz a default option
    # TODO: implement screen

    def __init__(
        self,
        name,
        disp_list,
        return_func,
        page_sz=8
    ):
        key_dict = dict(
            e=self.PageUp,
            d=self.PageDown,
            x=self.Exit
        )
        self.list_widget = scrollablelist.scrollablelist(
            disp_list,
            key_dict,
            page_sz
        )
        self.return_func = return_func
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
            self.return_func(chosen_element)

    def PageUp(self):
        return self.list_widget.GetPrevPage()

    def PageDown(self):
        return self.list_widget.GetNextPage()

    def Exit(self):
        self.exit = True
