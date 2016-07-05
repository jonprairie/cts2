class screen:
    def __init__(self, widgets, key_dict):
        '''TODO: add support for multiple widgets'''
        self.widgets = widgets
        self.focus_index = 0
        self.key_dict = key_dict
        self.display_only = False

    def PassInput(self, input):
        if input in self.key_dict.keys():
            self.key_dict[input]()
        else:
            self.widgets[
                self.focus_index
            ].PassInput(input)
