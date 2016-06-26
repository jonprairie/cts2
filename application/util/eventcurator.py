from cts2.application.events import *
from cts2.application.event import *
from string import *

message_events = set()

def BuildEventOutbox(event_name_list):
    temp_list = []
    for ev in event_name_list:
        if ev in message_events:
            pass #temp_list.append(messageevent.messageevent(ev))
        else:
            message_type = translate(ev, None, '_')
            y = eval(message_type + "." +)
            print message_type
