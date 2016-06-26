import events.messageevent as messageevent
import os


class displayhandler:
    # TODO: implement eventprocessor
    def __init__(self):
        self.read_sysin_ev = messageevent.messageevent(
            "read_sysin"
        )

    def ProcessEvent(self, ev):
        if ev.event_type == "display_screen":
            self.DisplayScreen(ev.screen)
        elif ev.event_type == "display_yes_or_no_message":
            response = self.GetYesOrNo(ev.message)
            ev.response = response
        elif ev.event_type == "display_input_message":
            response = self.GetInput(
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

    def DisplayScreen(
        self,
        screen
    ):
        self.DisplayString(
            str(screen),
            header=screen.name,
            pause=screen.display_only
        )
        while not screen.display_only and not screen.exit:
            self.event_handler.ProcessEvent(self.read_sysin_ev)
            screen.PassInput(self.read_sysin_ev.input)
            self.DisplayString(
                str(screen),
                header=screen.name,
                pause=screen.display_only
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

    def GetInput(self, msg, header="", pre_clear=True):
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
            inp = self.GetInput(msg)
        if inp[0] == "y":
            inp = "yes"
        else:
            inp = "no"
        return inp
