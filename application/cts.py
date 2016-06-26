import eventhandler
import event

event_handler = eventhandler.eventhandler()

exit_event = event.getexit()
menu_frame_event = event.menuframe()

while not exit_event.exit: 
	event_handler.ProcessEvent(menu_frame_event)
	event_handler.ProcessEvent(exit_event)