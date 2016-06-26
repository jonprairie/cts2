import cts2.game_instance.federation.federation as federation
import cts2.game_instance.federation.country as country

class federationhandler:
	def __init__(self, event_handler):
		self.event_handler = event_handler
		self.federation_list = []
		self.global_federation = federation.federation(
			self.event_handler,
			country.world
		)
		for cntry in country.country_list:
			self.federation_list.append(
				federation.federation(
					self.event_handler,
					cntry
				)
			)

	def ProcessEvent(self, event):
		pass
