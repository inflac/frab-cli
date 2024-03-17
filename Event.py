class Event:
    def __init__(self, guid, eid, date, start, duration, room, slug, url, recording, title, subtitle, track, etype, language, abstract, description, logo, persons, links, attachments):        
        self._guid = guid 
        self._id = eid
        self._date = date
        self._start = start
        self._duration = duration
        self._room = room
        self._slug = slug
        self._url = url
        self._recording = recording
        self._title = title
        self._subtitle = subtitle
        self._track = track
        self._type = etype
        self._language = language
        self._abstract = abstract
        self._description = description
        self._logo = logo
        self._persons = persons
        self._links = links
        self._attachments = attachments

    # Event class getter
    
    def get_guid(self):
        return self._guid

    def get_id(self):
        return self._id

    def get_date(self):
        return self._date

    def get_start(self):
        return self._start

    def get_duration(self):
        return self._duration

    def get_room(self):
        return self._room

    def get_slug(self):
        return self._slug

    def get_url(self):
        return self._url

    def get_recording(self):
        return self._recording

    def get_title(self):
        return self._title

    def get_subtitle(self):
        return self._subtitle

    def get_track(self):
        return self._track

    def get_type(self):
        return self._type

    def get_language(self):
        return self._language

    def get_abstract(self):
        return self._abstract

    def get_description(self):
        return self._description

    def get_logo(self):
        return self._logo

    def get_persons(self):
        return self._persons

    def get_links(self):
        return self._links

    def get_attachments(self):
        return self._attachments
    
    def get_event_xml(self):
        return self._event_xml
    
    # Additional getter
    def get_person_by_name(self, person_name):
        for person in self._persons:
            if person.get_name() == person_name: return person

    def get_persons_xml(self):
        persons_xml = ""
        for person in self._persons:
            persons_xml += person.get_person_xml()
        return persons_xml

    def get_event_xml(self):
        '''
        Create the event XML based on the given parameters.

        Return the event XML as string.
        '''

        event_xml = f'''
        <event guid='{self._guid}' id='{self._id}'>
        <date>{self._date}</date>
        <start>{self._start}</start>
        <duration>{self._duration}</duration>
        <room>{self._room.get_name()}</room>
        <slug>{self._slug}</slug>
        <url>{self._url}</url>
        <recording>
        <license></license>
        <optout>{self._recording}</optout>
        </recording>
        <title>{self._title}</title>
        <subtitle>{self._subtitle}</subtitle>
        <track>{self._track}</track>
        <type>{self._type}</type>
        <language>{self._language}</language>
        <abstract>{self._abstract}</abstract>
        <description>{self._description}</description>
        {self._logo}
        <persons>
        {self.get_persons_xml()}
        </persons>
        <links>{self._links}</links>
        <attachments>{self._attachments}</attachments>
        </event>
        '''

        return event_xml

    # Event class setter    
    def set_date(self, date):
        self._date = date

    def set_start(self, start):
        self._start = start

    def set_duration(self, duration):
        self._duration = duration

    def set_room(self, room):
        self._room = room

    def set_slug(self, slug):
        self._slug = slug

    def set_url(self, url):
        self._url = url

    def set_recording(self, recording):
        self._recording = recording
    
    def set_title(self, title):
        self._title = title

    def set_subtitle(self, subtitle):
        self._subtitle = subtitle

    def set_track(self, track):
        self._track = track

    def set_type(self, type):
        self._type = type

    def set_language(self, language):
        self._language = language

    def set_abstract(self, abstract):
        self._abstract = abstract
    
    def set_description(self, description):
        self._description = description

    def set_logo(self, logo):
        self._logo = logo

    def set_persons(self, persons):
        self._persons = persons

    def set_links(self, links):
        self._links = links

    def set_attachments(self, attachments):
        self._attachments = attachments
    
    def set_event_xml(self, event_xml):
        self._event_xml = event_xml