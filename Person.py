class Person:
    def __init__(self, conference, name, pid):
        self._conference = conference
        self._name = name
        self._id = pid

    #Person class getter
    def get_conference(self):
        return self._conference    

    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id

    # Additional getter
    def get_person_xml(self):
        return f"<person id='{self._id}'>{self._name}</person>\n"

    # Event class setter
    def set_name(self, name):
        self._name = name