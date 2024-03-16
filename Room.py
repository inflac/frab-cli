class Room:
    def __init__(self, name, conference):
        self._conference = conference
        self._name = name
        self._events = []

    # Room class getter 
    def get_conference(self):
        return self._conference

    def get_name(self):
        return self._name
    
    def get_events(self):
        return self._events
    
    # Additional getter
    def get_room_xml(self):
        for i in range(10): print("!!! NOT IMPLEMENTED !!!")
        '''
        Create the room XML based on the given parameters.

        Return the room XML as string.
        '''

        room_xml = f'''
        <room name='{self._room_name}'>
        <!-- NEW_EVENT -->
        </room>
        '''

        return room_xml

    # Room class setter
    ## Setter need to modify room_xml