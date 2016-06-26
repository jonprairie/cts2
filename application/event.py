import random

class event:
	def __init__(self,event_type,pre_children=[],post_children=[]):
		self.event_type=event_type
		self.pre_children=pre_children
		self.post_children=post_children
	def PreProcess(self):
		pass
	def PostProcess(self):
		pass
	def Initialize(self):
		pass
	def CleanUp(self):
		pass

class getexit(event):
	"""returns whether application should exit"""
	def __init__(self):
		event.__init__(self,"get_exit")
		self.exit=""

class makeexit(event):
	def __init__(self):
		event.__init__(self,"make_exit")

class initgameinstancehandlers(event):
	def __init__(self):
		event.__init__(self,"init_game_instance_handlers")

class displaystringtable(event):
	def __init__(self, st, header="Chess Tournament Sim", line_num=0, pre_clear=True, pause=True):
		event.__init__(self,"display_string_table")
		self.st = st
		self.header = header
		self.line_num = line_num
		self.pre_clear = pre_clear
		self.pause = pause

class displayinputmessage(event):
	def __init__(self, msg, header="", pre_clear=True):
		event.__init__(self,"display_input_message")
		self.msg = msg
		self.header = header
		self.pre_clear = pre_clear

class displayyesornomessage(event):
	"""will return either a 'yes' or a 'no' in self.response"""
	def __init__(self, message):
		event.__init__(self,"display_yes_or_no_message")
		self.message = message
		self.response = ""

class menuframe(event):
	"""runs next frame of the menu"""
	def __init__(self):
		event.__init__(self,"menu_frame")

class getdatefromjulianoffset(event):
	def __init__(self,julian_offset):
		event.__init__(self,"get_date_from_julian_offset")
		self.julian_offset=julian_offset
		self.date=""

class getdatelistfromjulianoffsetlist(event):
	def __init__(self,julian_offset_list):
		event.__init__(self,"get_date_list_from_julian_offset_list")
		self.julian_offset_list = julian_offset_list
		self.date_list=""

	def Initialize(self):
		self.pre_children = [getdatefromjulianoffset(x) for x in self.julian_offset_list]

	def CleanUp(self):
		self.date_list=[x.date for x in self.pre_children]

class addtournamenttowaitinglist(event):
	def __init__(self,tournament):
		event.__init__(self,"add_tournament_to_waiting_list")
		self.tournament=tournament

class addtournamenttonewlist(event):
	def __init__(self,tournament):
		event.__init__(self,"add_tournament_to_new_list")
		self.tournament=tournament

class getnonstartedtournaments(event):
	def __init__(self):
		event.__init__(self,"get_non_started_tournament_list")
		self.non_started_tournament_list=""

class createtournament(event):
	"""I think I'm going to deprecate this and use a
	messageevent instead"""
	def __init__(self,name,start_julian_offset):
		event.__init__(self,"create_tournament")
		self.name=name
		self.start_julian_offset=start_julian_offset
		self.tournament=""

	def PostProcess(self):
		self.date_index_list = [x+self.start_julian_offset for x in self.tournament.GetDateIndexList()]
		self.post_children = [getdatelistfromjulianoffsetlist(self.date_index_list)]
		self.post_children.append(addtournamenttowaitinglist(self.tournament))

	def CleanUp(self):
		self.date_list = self.post_children[0].date_list
		self.tournament.AddStartDate(self.date_list[0])
		self.tournament.date_range = self.date_list
		#self.tournament.UpdateRow("date", str(self.tournament.date_range[0].GetDate()))
		#self.tournament.date_index_list=self.date_index_list
		for x in self.date_list:
			x.AddTournament(self.tournament)

class createrandomtournament(createtournament):
	def __init__(self):
		event.__init__(self,"create_random_tournament")
		self.start_julian_offset=random.randint(14,125)
		self.name=""
		self.tournament=""
