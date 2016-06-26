class exithandler:
	def __init__(self):
		self.exit = False

	def ProcessEvent(self, ev):
		if ev.event_type == "make_exit":
			self.exit = True
		if ev.event_type == "get_exit":
			ev.exit = self.exit