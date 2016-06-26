import cts2.application.util.eventprocessor as eventprocessor
import cts2.game_instance.calendar.date as date
import datetime
import calendar


class calendarhandler(eventprocessor.eventprocessor):
    def __init__(self, event_handler):

        # initialize module as an eventprocessor
        self.event_dict = dict(
            get_date_from_julian_offset=self.GetDateFromJulianOffset,
            register_for_maintenance=self.RegisterForMaintenance,
            advance_day=self.IncrementDay
        )
        eventprocessor.eventprocessor.__init__(
            self,
            self.event_dict,
            event_handler
        )

        self.current_date = datetime.date(
            self.default_options["start_year"],
            self.default_options["start_month"],
            self.default_options["start_day"]
        )

        self.current_date_index = 0
        self.date_list = []
        self.InitDateList()

        self.daily_list = []
        self.weekly_list = []
        self.monthly_list = []
        self.annually_list = []

    def GetDateFromJulianOffset(self, ev):
        ev.date = self.GetDate(ev.julian_offset)

    def InitDateList(self):

        current_date_ordinal = self.current_date.toordinal()
        for day in range(self.default_options["game_length"]):
            temp_date_1 = datetime.date.fromordinal(current_date_ordinal + day)
            temp_date_2 = date.date(date = temp_date_1)
            self.date_list.append(temp_date_2)

    def ExtendDateList(self, num_days):

        last_ordinal = self.date_list[len(self.date_list)-1].date.toordinal() + 1
        date_list_addition = [date.date(date=datetime.date.fromordinal(last_ordinal+x)) for x in range(num_days)]
        self.date_list.extend(date_list_addition)

    #Get Functions
    def GetCurrentDate(self):
        return self.GetDate(0)

    def GetDate(self, date_offset):
        """returns the date corresponding to the current date's index + date_index"""

        date_index = self.current_date_index + date_offset
        if date_index >= len(self.date_list):
            self.ExtendDateList(date_index-len(self.date_list)+1)
        return self.date_list[date_index]

    def GetDateRange(self, start_date, index_list):
        """takes a start date and a list of indexes and returns a list of the dates corresponding to the
        indexes, relative to the start date's index"""

        ret_list = []
        start_date_index = self.date_list.index(start_date)
        return [self.GetDate(x+start_date_index) for x in index_list]

    def RegisterForMaintenance(self, ev):
        if ev.daily:
            self.daily_list.append(ev.subscriber)
        if ev.weekly:
            self.weekly_list.append(ev.subscriber)
        if ev.monthly:
            self.monthly_list.append(ev.subscriber)
        if ev.annually:
            self.annually_list.append(ev.subscriber)

    #Test Functions
    def IsWeek(self):
        ret_bool = self.current_date_index % 7
        return not ret_bool

    def IsMonth(self):
        ret_bool = self.current_date_index % 30
        return not ret_bool

    def IsYear(self):
        return False

    #Maintenance Functions
    def IncrementDay(self, ev):
        for days in range(ev.num_days):
            self.current_date_index += 1
            self.ExtendDateList(1)

            for obj in self.daily_list:
                self.LogMessage(
                    str(obj) + " daily maintenance, day " + str(self.current_date_index)
                )
                obj.DailyMaintenance(self.current_date_index)
            if self.IsWeek():
                for obj in self.weekly_list:
                    self.LogMessage(
                        str(obj) + " weekly maintenance, day " + str(self.current_date_index)
                    )
                    obj.WeeklyMaintenance(self.current_date_index)
            if self.IsMonth():
                for obj in self.monthly_list:
                    obj.MonthlyMaintenance(self.current_date_index)
            if self.IsYear():
                for obj in self.annually_list:
                    obj.YearlyMaintenance(self.current_date_index)
