"""
this is a widget container widget.

allows scrolling between widgets, focusing (and displaying)
one at a time.
"""
import widget


class sidescrollwidget(widget.widget):
    def __init__(
        self, widget_list, key_dict=dict(
            scroll_left="<",
            scroll_right=">",
        )
    ):
        self.widget_list = widget_list
        self.focus_index = 0
        widget.widget.__init__(self)
        self.AddKeyDict(
            dict([
                (key_dict["scroll_left"], self.ScrollLeft),
                (key_dict["scroll_right"], self.ScrollRight)
            ])
        )

    def ProcessesInput(self, inp):
        if widget.widget.ProcessesInput(self, inp):
            return True
        elif self.widget_list[self.focus_index].ProcessesInput(inp):
            return True
        else:
            return False

    def ProcessInput(self, inp):
        if widget.widget.ProcessesInput(self, inp):
            widget.widget.ProcessInput(self, inp)
        else:
            self.DelegateInput(inp)

    def DelegateInput(self, inp):
        return self.GetFocusedWidget().ProcessInput(inp)

    def GetFocusedWidget(self):
        return self.widget_list[self.focus_index]

    def ScrollLeft(self):
        self.focus_index -= 1
        if self.focus_index < 0:
            self.focus_index = len(self.widget_list) - 1

    def ScrollRight(self):
        self.focus_index += 1
        if self.focus_index > len(self.widget_list) - 1:
            self.focus_index = 0

    def ToString(self):
        return self.widget_list[self.focus_index].ToString()
