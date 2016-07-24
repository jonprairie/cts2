import menuhandler
import exithandler
import cts2.application.handlers.optionhandler as optionhandler
import cts2.display.displayhandler as displayhandler
import cts2.application.handlers.tournamenthandler as tournamenthandler
import cts2.application.handlers.calendarhandler as calendarhandler
import cts2.application.handlers.createplayerhandler as createplayerhandler
import cts2.application.handlers.playerhandler as playerhandler
import cts2.application.handlers.federationhandler as federationhandler
import cts2.application.handlers.loghandler as loghandler
import cts2.application.input.inputhandler as inputhandler


class eventhandler:
    '''TODO: refactor handlers into modules'''
    def __init__(self):

        # define these first so the other event processing
        # modules can access them on __init__
        self.handler_registry = dict(
            log_handler=loghandler.loghandler(self)
        )
        self.event_registry = dict(
            log_message="log_handler"
        )
        self.handler_registry.update(dict(
            option_handler=optionhandler.optionhandler(self)
        ))
        self.event_registry.update(dict(
            get_default_options="option_handler"
        ))

        # initialize the other application-wide event processors
        self.handler_registry.update(dict(
            menu_handler=menuhandler.menuhandler(self),
            exit_handler=exithandler.exithandler(),
            display_handler=displayhandler.displayhandler(),
            input_handler=inputhandler.inputhandler(self),
        ))

        # shouldn't be needed once all event processors implement
        # the cts2.util.eventprocessor class
        for h in self.handler_registry.values():
            self.LinkEventHandler(h)

        # create the mapping from events to event processors
        self.event_registry.update(
            dict(
                get_exit="exit_handler",
                make_exit="exit_handler",
                menu_frame="menu_handler",
                init_game_instance_handlers="event_handler",
                create_tournament="tournament_handler",
                create_random_tournament="tournament_handler",
                add_tournament_to_waiting_list="tournament_handler",
                add_tournament_to_new_list="tournament_handler",
                get_non_started_tournament_list="tournament_handler",
                get_current_tournament_list="tournament_handler",
                # simulate_game="game_sim_handler",
                # build_schedule="schedule_handler",
                get_date_from_julian_offset="calendar_handler",
                register_for_maintenance="calendar_handler",
                advance_day="calendar_handler",
                get_date_list_from_julian_offset_list="dummy",
                display_string_table="display_handler",
                display_input_message="display_handler",
                display_yes_or_no_message="display_handler",
                display_screen="display_handler",
                display_string="display_handler",
                read_sysin="input_handler",
                create_player="create_player_handler",
                create_player_list="create_player_handler",
                get_player_list="player_handler",
                log_message="log_handler"
            )
        )

    def InitGameInstanceHandlers(self):
        # Update create_player_handler first so other modules can create
        # players on __init__
        self.handler_registry.update(
            create_player_handler=createplayerhandler.createplayerhandler(
                self
            ),
            calendar_handler=calendarhandler.calendarhandler(self)
        )
        self.handler_registry.update(
            tournament_handler=tournamenthandler.tournamenthandler(self),
            # game_sim_handler=gamesim.gamesim(self),
            player_handler=playerhandler.playerhandler(self),
            federation_handler=federationhandler.federationhandler(self)
            # schedule_handler=schedulehandler.schedulehandler()
        )

    def ProcessEvent(self, event):
        event.Initialize()
        if event.pre_children:
            for ce in event.pre_children:
                self.ProcessEvent(ce)
        event.PreProcess()
        handler_key = self.event_registry[event.event_type]
        if handler_key != "dummy" and handler_key != "event_handler":
            self.handler_registry[handler_key].ProcessEvent(event)
        elif handler_key == "event_handler":
            if event.event_type == "init_game_instance_handlers":
                self.InitGameInstanceHandlers()
        event.PostProcess()
        if event.post_children:
            for ce in event.post_children:
                self.ProcessEvent(ce)
        event.CleanUp()

    def LinkEventHandler(self, obj):
        obj.event_handler = self
