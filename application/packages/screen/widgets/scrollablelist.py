"""
scrollable display list widget
"""
import widget


class scrollablelist(widget.widget):
    def __init__(
        self,
        name,
        disp_list,
        key_dict=dict(
            scroll_up="e",
            scroll_down="d"
        ),
        page_size=8
    ):
        widget.widget.__init__(self, name=name)
        self.AddKeyDict(
            dict([
                (key_dict["scroll_up"], self.GetPrevPage),
                (key_dict["scroll_down"], self.GetNextPage)
            ])
        )
        self.disp_list = disp_list
        self.page_size = page_size
        self.list_len = len(self.disp_list)
        self.line_index = 0

    def SetDispList(self, dl):
        self.disp_list = dl
        self.list_len = len(self.disp_list)

    def ToString(self):
        return "\n".join(
            [str(obj) for obj in self.GetCurrentPage()]
        )

    def IsFirstPage(self):
        if self.line_index < self.page_size:
            return True
        else:
            return False

    def IsLastPage(self):
        if self.line_index + self.page_size >= self.list_len:
            return True
        else:
            return False

    def GetCurrentPage(self):
        return self.GetPageObj(self.line_index)

    def GetPage(self, line_num):
        self.line_index = line_num
        if self.IsLastPage():
            ret_list = [
                str(s) for s in self.disp_list[
                    self.line_index:
                ]
            ]
        else:
            ret_list = [
                str(s) for s in self.disp_list[
                    self.line_index:
                    self.line_index + self.page_size
                ]
            ]
        return ret_list

    def GetPageObj(self, line_num):
        self.line_index = line_num
        if self.IsLastPage():
            ret_list = self.disp_list[
                self.line_index:
            ]
        else:
            ret_list = self.disp_list[
                self.line_index:
                self.line_index + self.page_size
            ]
        return ret_list

    def GetNextPage(self):
        if self.IsLastPage():
            return self.GetPage(self.list_len-1)
        else:
            return self.GetPage(
                self.line_index + self.page_size
            )

    def GetPrevPage(self):
        if self.IsFirstPage():
            return self.GetPage(0)
        else:
            return self.GetPage(
                self.line_index - self.page_size
            )
