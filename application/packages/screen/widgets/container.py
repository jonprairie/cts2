"""
container widget for holding other widgets.
"""
import widget


class container(widget.widget):
    def __init__(
        self, widget_list, key_dict=None, name=""
    ):
        widget.widget.__init__(self, name=name)
        self.AddKeyDict(key_dict)
        self.widget_list = widget_list
        self.focus_index = 0

    def ProcessesInput(self, inp):
        if widget.widget.ProcessesInput(self, inp):
            return True
        elif self.GetFocusedWidget().ProcessesInput(inp):
            return True
        else:
            return False

    def ProcessInput(self, inp):
        if widget.widget.ProcessesInput(self, inp):
            try:
                widget.widget.ProcessInput(self, inp)
            except Exception as e:
                self.ProcessError(e)
        else:
            try:
                self.DelegateInput(inp)
            except Exception as e:
                self.ProcessError(e)

    def UpdateWidgetList(self, widget_list):
        self.widget_list = widget_list

    def DelegateInput(self, inp):
        return self.GetFocusedWidget().ProcessInput(inp)

    def GetFocusedWidget(self):
        return self.widget_list[self.focus_index]

    def ProcessError(self, e):
        import pdb; pdb.set_trace
