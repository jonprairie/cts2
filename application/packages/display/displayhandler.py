import cts2.application.events.messageevent as messageevent
import cts2.application.util.pkg as pkg
import os


class displayhandler(pkg.pkg):
    # TODO: implement eventprocessor
    def __init__(self, api):
        self.read_sysin_ev = messageevent.messageevent(
            "read_sysin"
        )
        pkg.pkg.__init__(
            self,
            api,
            "display_handler",
            [
                "add_screen",
                "pop_screen",
                "display",
                "get_top_screen"
            ],
            ["log_msg"]
        )
        self.screen_stack = []

    def ProcessEvent(self, ev):
        if ev.event_type == "display_screen":
            self.DisplayScreen(ev.screen)
        elif ev.event_type == "display_yes_or_no_message":
            response = self.GetYesOrNo(ev.message)
            ev.response = response
        elif ev.event_type == "display_input_message":
            response = self.DisplayInputMessage(
                ev.msg,
                header=ev.header,
                pre_clear=ev.pre_clear
            )
            ev.response = response
        elif ev.event_type == "display_string_table":
            self.DisplayStringTable(
                ev.st,
                header=ev.header,
                pre_clear=ev.pre_clear,
                pause=ev.pause,
                line_num=ev.line_num
            )
        elif ev.event_type == "display_string":
            self.DisplayString(ev.st)

    def AddScreen(self, screen):
        self.screen_stack.append(screen)

    def PopScreen(self):
        self.screen_stack.pop()

    def GetTopScreen(self):
        return self.screen_stack[-1]

    def Display(self):
        '''filter exited screens from display stack, then
        display top screen'''
        exit_stack = filter(
            lambda x: x.GetExit(),
            self.screen_stack
        )
        self.screen_stack = filter(
            lambda x: not x.GetExit(),
            self.screen_stack
        )
        for scr in exit_stack:
            scr.exit = False
        self.DisplayScreen(
            self.screen_stack[-1]
        )

    def DisplayScreen(
        self,
        screen
    ):
        self.DisplayString(
            str(screen),
            pause=False
        )

    def DisplayStringTable(
        self,
        st,
        header,
        pre_clear=True,
        pause=True,
        line_num=0
    ):
        self.DisplayString(
            st.ToString(row_num=line_num),
            header=header,
            pre_clear=pre_clear,
            pause=pause
        )

    def DisplayString(self, st, header="", pre_clear=True, pause=True):
        if pre_clear:
            os.system("CLS")
        if header:
            print header, '\n\n'
        print st
        if pause:
            os.system("PAUSE")

    def DisplayInputMessage(self, msg, header="", pre_clear=True):
        self.DisplayString(
            msg,
            header=header,
            pre_clear=pre_clear,
            pause=False
        )
        return raw_input("\n--> ")

    def GetYesOrNo(self, msg):
        inp = ""
        while inp not in ["yes", "y", "no", "n"]:
            inp = self.DisplayInputMessage(msg)
        if inp[0] == "y":
            inp = "yes"
        else:
            inp = "no"
        return inp
