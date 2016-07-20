import eventhandler
import event


def main():
    event_handler = eventhandler.eventhandler()

    exit_event = event.getexit()
    menu_frame_event = event.menuframe()

    while not exit_event.exit:
        event_handler.ProcessEvent(menu_frame_event)
        event_handler.ProcessEvent(exit_event)

if __name__ == '__main__':
    main()
