import cts2.application.events.messageevent as messageevent

class maintenancesubscriber:
    def __init__(self,daily,weekly,monthly,annually):
        self.maintenance_register_event = messageevent.messageevent(
            "register_for_maintenance"
        )
        self.maintenance_register_event.daily = daily
        self.maintenance_register_event.weekly = weekly
        self.maintenance_register_event.monthly = monthly
        self.maintenance_register_event.annually = annually
        self.maintenance_register_event.subscriber = self
        self.event_handler.ProcessEvent(self.maintenance_register_event)
