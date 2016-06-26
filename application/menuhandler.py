import cts2.application.util.eventprocessor as eventprocessor
import event
import menu.arch.node as node
import menu.arch.menudriver as menudriver
import menu.gameinstancemenu as gameinstancemenu

class menuhandler(eventprocessor.eventprocessor):
    def __init__(self, event_handler):

		# initialize module as an eventprocessor
        self.event_dict = dict(menu_frame=self.MenuMux)
        eventprocessor.eventprocessor.__init__(self,self.event_dict,event_handler)

        self.BuildMainMenu()
        self.exit_question = event.displayyesornomessage("Are you sure that you want to exit?")
        self.disp_menu_frame = event.displayinputmessage(self.menu_driver.GetStringTable())
        self.init_game_instance_handlers = event.initgameinstancehandlers()
        self.menu_stack = [self]

    def MenuMux(self,ev):
        temp_menu = self.menu_stack.pop()
        if temp_menu != self and temp_menu.exit:
            temp_menu = self.menu_stack.pop()
        self.menu_stack.append(temp_menu)
        temp_menu.MenuFrame()

    def MenuFrame(self):
        self.event_handler.ProcessEvent(self.disp_menu_frame)
        self.menu_driver.Select(self.disp_menu_frame.response)

    def BuildMainMenu(self):
        en1 = node.exteriornode("exit", self.MakeExit)
        en2 = node.exteriornode("new game", self.NewGame)
        en3 = node.exteriornode("load game", self.LoadGame)
        menu_list = [en1, en2, en3]
        self.menu_driver=menudriver.menudriver("Chess Tournament Sim", menu_list)

    def MakeExit(self):
        self.event_handler.ProcessEvent(self.exit_question)
        if self.exit_question.response == "yes":
            exit = event.makeexit()
            self.event_handler.ProcessEvent(exit)

    def NewGame(self):
        self.event_handler.ProcessEvent(self.init_game_instance_handlers)
        temp_menu = gameinstancemenu.gameinstancemenu()
        temp_menu.event_handler = self.event_handler
        self.menu_stack.append(temp_menu)

    def LoadGame(self):
        pass

    def GetCurrentTournamentList(self):
        gctl_event = event.getstartedtournaments()
        event_handler.ProcessEvent(gctl_event)
        return gctl_event.started_tournament_list

    def GetFutureTournamentList(self):
        gftl_event = event.getnonstartedtournaments()
        event_handler.ProcessEvent(gftl_event)
        return gftl_event.non_started_tournament_list
