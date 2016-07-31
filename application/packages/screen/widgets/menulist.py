"""
widget that executes a function based on the
selection of an option from a list.
"""
import scrollablelist
import container


class menulist(container.container):
    def __init__(
        self, nm, sel_map,
        sel_keys=(
            "asdfjkl;ghqweruioptyzxcvm,./bn" +
            "ASDFJKL;GHQWERUIOPTYZXCVM,./BN"
        ),
        sel_order=None,
        scroll_keys=dict(
            scroll_up="e",
            scroll_down="d"
        ),
        pg_size=8
    ):
        self.sel_map = sel_map
        self.sel_keys = sel_keys
        self.scroll_keys = scroll_keys
        if sel_order is None:
            self.sel_order = dict(
                enumerate(sel_map.keys())
            )
        else:
            self.sel_order = sel_order

        for k in scroll_keys.values():
            if k in self.sel_keys:
                self.sel_keys = self.sel_keys[
                    :self.sel_keys.index(k)
                ] + self.sel_keys[
                    self.sel_keys.index(k)+1:
                ]

        self.scroll_list = scrollablelist.scrollablelist(
            nm, self.sel_order.keys(),
            self.scroll_keys, pg_size
        )
        container.container.__init__(
            self, [self.scroll_list], name=nm
        )
        self.SetKeyDict()

    def UpdateMappings(
        self, sel_map, sel_order=None
    ):
        self.sel_map = sel_map
        if sel_order is None:
            self.sel_order = dict(
                enumerate(sel_map.keys())
            )
        else:
            self.sel_order = sel_order
        self.scroll_list = scrollablelist.scrollablelist(
            self.name,
            self.sel_order.keys(),
            key_dict=self.scroll_keys,
            page_size=self.scroll_list.page_size
        )
        self.widget_list = [self.scroll_list]
        self.SetKeyDict()

    def ToString(self):
        return "\n".join(
            [self.name] +
            [
                str(self.sel_keys[i]) + " --- " +
                str(self.sel_order[k])
                for i, k in enumerate(
                    self.scroll_list.GetCurrentPage()
                )
            ]
        )

    def DelegateInput(self, inp):
        container.container.DelegateInput(self, inp)
        self.SetKeyDict()

    def SetKeyDict(self):
        self.AddKeyDict(
            dict([
                (
                    self.sel_keys[i],
                    self.sel_map[
                        self.sel_order[k]
                    ]
                ) for i, k in enumerate(
                    self.scroll_list.GetCurrentPage()
                )
            ])
        )
