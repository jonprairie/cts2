"""
widget to search list of objects using regular expressions
"""
import widget
import re


class searchlist(widget.widget):
    def __init__(
        self, name, search_list,
        str_func=lambda x: str(x)
    ):
        self.search_list = search_list
        self.str_func = str_func
        widget.widget.__init__(self, name)

    def ProcessesInput(self, inp):
        try:
            re.compile(inp)
            return True
        except re.error:
            return False

    def ProcessInput(self, inp):
        return [
            e for e in self.search_list if re.search(
                inp, self.str_func(e)
            )
        ]
