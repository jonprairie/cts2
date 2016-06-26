import widget


class scrollablelist(widget.widget):
    def __init__(
        self,
        disp_list,
        key_dict,
        page_size
    ):
        widget.widget.__init__(self, key_dict)
        self.disp_list = disp_list
        self.page_size = page_size
        self.list_len = len(self.disp_list)
        self.line_index = 0

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
        return self.GetPage(self.line_index)

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
