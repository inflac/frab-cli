class Day:
    def __init__(self, date, end, index, start):
        self._date = date
        self._end = end
        self._index = index
        self._start = start
        self._events = []
    
    # Day class getter
    def get_date(self):
        return self._date
    
    def get_end(self):
        return self._end

    def get_index(self):
        return self._index

    def get_start(self):
        return self._start
    
    # Additional getter
    def get_day_xml(self, conference):
        day_xml = ""
        for room in conference.get_rooms():
            room_xml = f"<room name='{room.get_name()}'>\n"
            for event in self._events:
                if room.get_name() == event.get_room().get_name():
                    room_xml += event.get_event_xml()
            room_xml += "</room>\n"
            day_xml += room_xml

        return f'''
        <day date='{self._date.strftime('%Y-%m-%d')}' end='{self._end}' index='{self._index}' start='{self._start}'>
        {day_xml}
        </day>
        '''

    # Conference class setter
    ## Setter need to modify conference_xml
    def set_events(self, events):
        self._events = events