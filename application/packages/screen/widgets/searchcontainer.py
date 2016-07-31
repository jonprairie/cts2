"""
extends sidescrollwidget, this is the container for the
searchlist widget. supports viewing results and flipping
back to search page.
"""
import sidescrollwidget
import searchlist
import menulist


class searchcontainer(
    sidescrollwidget.sidescrollwidget
):
    def __init__(self, list_name, search_list, select_func):
        self.select_func = select_func
        self.search_list = search_list
        self.menu_list_w = menulist.menulist(
            list_name + " results:",
            dict([
                (p, lambda: select_func(p))
                for p in self.search_list
            ])
        )
        self.search_list_w = searchlist.searchlist(
            list_name + " search:",
            search_list
        )
        sidescrollwidget.sidescrollwidget.__init__(
            self, [self.search_list_w, self.menu_list_w]
        )

    def DelegateInput(self, inp):
        res = sidescrollwidget.sidescrollwidget.DelegateInput(
            self, inp
        )
        if res and self.GetFocusedWidget() is self.search_list_w:
            self.UpdateMenuList(res)
            self.ScrollRight()

    def UpdateMenuList(self, results):
        self.menu_list_w.UpdateMappings(
            dict([
                (r, self.ProjectSelectFunc(r))
                for r in results
            ])
        )

    def ProjectSelectFunc(self, r):
        return lambda: self.select_func(r)
