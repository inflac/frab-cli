class Conference:
    def __init__(self, title, acronym, start, end, days, timeslot_duration, base_url):
        self._title = title
        self._acronym = acronym
        self._start = start
        self._end = end
        self._days = days
        self._timeslot_duration = timeslot_duration
        self._base_url = base_url
        self._rooms = []
        self._days_obj = []
        self._persons = []

    # Conference class getter
    def get_title(self):
        return  self._title
    
    def get_acronym(self):
        return  self._acronym
    
    def get_start(self):
        return  self._start
    
    def get_end(self):
        return  self._end
    
    def get_days(self):
        return  self._days
    
    def get_timeslot_duration(self):
        return  self._timeslot_duration
    
    def get_base_url(self):
        return  self._base_url
    
    def get_rooms(self):
        return self._rooms

    def get_conference_xml(self):
        return self._conference_xml
    
    def get_days_obj(self):
        return self._days_obj
    
    def get_persons(self):
        return self._persons

    # Additional getter
    def get_room_by_name(self, room_name):
        for room in self._rooms:
            if room.get_name() == room_name: return room
        
    def has_room(self, room_name:str):
        return self.get_room_by_name(room_name) in self._rooms
    
    def get_room_names(self):
        return [room.get_name() for room in self._rooms]

    def get_person_by_name(self, person_name):
        for person in self._persons:
            if person.get_name() == person_name: return person
        return        

    def get_conference_xml(self):
        '''
        Create the conference XML based on the given parameters.

        Return the conference XML as string.
        '''

        conference_xml = f'''
        <conference>
        <acronym>{self._acronym}</acronym>
        <title>{str(self._title)}</title>
        <start>{str(self._start.date())}</start>
        <end>{str(self._end.date())}</end>
        <days>{str(self._days)}</days>
        <timeslot_duration>{self._timeslot_duration}</timeslot_duration>
        <base_url>{self._base_url}</base_url>
        </conference>
        '''
        return conference_xml

    # Conference class setter
    def set_title(self, title):
        self._title = title
        self.set_conference_xml()
    
    def set_acronym(self, acronym):
        self._acronym = acronym
        self.set_conference_xml()
    
    def set_start(self, start):
        self._start = start
        self.set_conference_xml()
    
    def set_end(self, end):
        self._end = end
        self.set_conference_xml()
    
    def set_days(self, days):
        self._days = days
        self.set_conference_xml()
    
    def set_timeslot_duration(self, timeslot_duration):
        self._timeslot_duration = timeslot_duration
    
    def set_base_url(self, base_url):
        self._base_url = base_url
        self.set_conference_xml()
    
    def set_rooms(self, rooms):
        self._rooms = rooms
    
    def set_days_obj(self, days_obj):
        self._days_obj = days_obj

    # Additional setter
    def add_person(self, person):
        self._persons.append(person)

    def add_persons(self, persons):
        for person in persons: self._persons.append(person)