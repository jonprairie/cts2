import cts2.application.util.eventprocessor as eventprocessor
import cts2.stats.genplayer as genplayer

class createplayerhandler(eventprocessor.eventprocessor):
    def __init__(self, event_handler):

		# initialize module as an eventprocessor
        self.event_dict = dict(
            create_player=self.GenPlayer,
            create_player_list=self.GenPlayerList
        )
        eventprocessor.eventprocessor.__init__(self,self.event_dict,event_handler)

    def GenPlayer(self, ev):
        new_player = genplayer.GenPlayer(self.default_options)
        ev.player = new_player

    def GenPlayerList(self, ev):
        ret_list = []
        for p in range(ev.num_players):
            ret_list.append(genplayer.GenPlayer(self.default_options))
        ev.player_list = ret_list
