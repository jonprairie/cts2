"""
extends sidescrollwidget, this is the container for the
searchlist widget. supports viewing results and flipping
back to search page.
"""
import sidescrollwidget
import searchlist
import scrollablelist


class searchcontainer(
    sidescrollwidget.sidescrollwidget
):
    def __init__(self, list_name, search_list, str_func):
        self.scroll_list_w = scrollablelist.scrollablelist(
            list_name + " results:",
            []
        )
        self.search_list_w = searchlist.searchlist(
            list_name + " search:",
            search_list,
            str_func
        )
        sidescrollwidget.sidescrollwidget.__init__(
            self, [self.search_list_w, self.scroll_list_w]
        )

    def DelegateInput(self, inp):
        res = sidescrollwidget.sidescrollwidget.DelegateInput(
            self, inp
        )
        if res and self.GetFocusedWidget() is self.search_list_w:
            self.scroll_list_w.SetDispList(res)
            self.ScrollRight()
