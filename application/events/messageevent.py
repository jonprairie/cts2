import cts2.application.event as event

class messageevent(event.event):
    def __init__(self, event_type):
        event.event.__init__(self, event_type)
