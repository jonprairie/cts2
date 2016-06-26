import cts2.application.util.eventprocessor as eventprocessor
import cts2.application.util.maintenancesubscriber as maintenancesubscriber
import cts2.application.util.stringtable as stringtable
import cts2.application.events.messageevent as messageevent
import cts2.database.tournamentnameinterface as tournamentnameinterface
import cts2.game_instance.tournament.drrinvitational as drrinvitational
import random


class tournamenthandler(
    eventprocessor.eventprocessor,
    maintenancesubscriber.maintenancesubscriber
):

    def __init__(self, event_handler):

        self.event_dict = dict(
            create_tournament=self.CreateTournament,
            create_random_tournament=self.CreateRandomTournament,
            get_current_tournament_list=self.GetCurrentTournaments,
            get_non_started_tournament_list=self.GetFutureTournaments
        )
        eventprocessor.eventprocessor.__init__(
            self,
            self.event_dict,
            event_handler
        )
        maintenancesubscriber.maintenancesubscriber.__init__(
            self, True, False, False, False
        )

        self.get_player_list = messageevent.messageevent("get_player_list")
        self.sim_game = messageevent.messageevent("simulate_game")
        self.tournament_list = []

    def CreateTournament(self, ev):
        self.CreateRandomTournament(ev)

    def CreateRandomTournament(self, ev):
        start_date = random.randint(15, 365)
        name = tournamentnameinterface.GenRandTournamentName()
        new_tournament = drrinvitational.drrinvitational(
            name,
            start_date,
            self.default_options["round_robin_player_range"]
        )
        self.LogMessage("created tournament: "+str(new_tournament))
        self.tournament_list.append(new_tournament)
        ev.new_tournament = new_tournament

    def GetCurrentTournaments(self, ev):
        ev.tournament_list = self.tournament_list

    def GetFutureTournaments(self, ev):
        ev.tournament_list = self.tournament_list

    def SendInvites(self, t):
        random.shuffle(
            self.get_player_list.player_list
        )
        for p in self.get_player_list.player_list:
            if t.SendInvite(p):
                self.LogMessage(str(t) + " sent invite to " + str(p))
            else:
                self.LogMessage(str(t) + " skipped over " + str(p))
            if t.InvitesFull():
                break

    def DailyMaintenance(self, date):
        self.event_handler.ProcessEvent(self.get_player_list)
        for t in self.tournament_list:
            if not t.finished and not t.started and t.sends_invites:
                self.SendInvites(t)
            if int(t.start_julian_date) == int(date):
                if t.HasEnoughPlayers():
                    t.started = True
                else:
                    self.LogMessage(
                        str(t) + " cancelling, needs " +
                        str(t.num_player_range[0]) + " players, " +
                        "only has " + str(len(t.player_list))
                    )
                    t.CancelTournament()
            if t.started and not t.schedule_finished:
                t.BuildSchedule()
                self.LogMessage(" schedule built: \n" + "\n".join(str(r) for r in t.schedule))
            if t.started and not t.finished:
                t.PlayRound()
                self.LogMessage(" simulated round: \n" + "\n".join(str(r) for r in t.schedule))
            if not t.started and not t.cancel and int(date) > int(t.start_julian_date):
                self.LogMessage(
                    str(t) + " error, start date is " +
                    str(t.start_julian_date) +
                    " today is " + str(date)
                )
