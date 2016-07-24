import cts2.application.events.messageevent as messageevent

class logger:
    def __init__(self):
        self.log_message_event = messageevent.messageevent("log_message")
        self.log_message_event.sender = self
        self.LogMessage("started")

    def LogMessage(self, msg):
        self.log_message_event.message = msg
        self.event_handler.ProcessEvent(self.log_message_event)
