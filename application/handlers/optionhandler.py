class optionhandler:
	def __init__(self, event_handler):

		# initialize module as an eventprocessor
		self.event_dict = dict(
			get_default_options=self.GetDefaultOptions
		)

		#dictionary of default game options
		self.options_dict = dict(
			#human player options
			real_player_elo = 1800,
			corresponding_elo = 2650,

			#cpu player options
			num_initial_cpu_players = 1000,
			elo = 2400,
			player_fame = 50,

			#player generation options
			play_strength_mu = 2500,
			play_strength_sigma = 100,

			#calendar options
			game_length = 730, #in days, 730 = 2 years
			start_year = 2015,
			start_month = 1,
			start_day = 18,

			#chess game options
			time_control = (45,0,0,45),

			#tournament options
			tournament_prestige = 50,
			tournament_prestige_decay_factor = 1,
			tournament_open = False,
			tournament_rounds = 7,
			tournament_rest_days = 2,
			tournament_type = "round robin",
			double_rr = False,
			round_robin_player_range = (4, 12),
			swiss_player_range = (8, 100)
		)

	def ProcessEvent(self, ev):
		self.event_dict[ev.event_type](ev)

	def GetDefaultOptions(self, ev):
		ret_dict = dict()
		if ev.option_keys:
			for k in ev.option_keys:
				ret_dict.update(
					(k, self.options_dict[k])
				)
		else:
			ret_dict = self.options_dict
		ev.option_dict = ret_dict
