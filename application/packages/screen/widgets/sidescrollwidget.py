"""
this is a widget container widget.

allows scrolling between widgets, focusing (and displaying)
one at a time.
"""
import container


class sidescrollwidget(container.container):
    def __init__(
        self, widget_list, key_dict=dict(
            scroll_left="<",
            scroll_right=">",
        )
    ):
        container.container.__init__(
            self,
            widget_list,
            key_dict=dict([
                (key_dict["scroll_left"], self.ScrollLeft),
                (key_dict["scroll_right"], self.ScrollRight)
            ])
        )

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
