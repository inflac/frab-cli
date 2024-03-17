from datetime import datetime, timedelta
import re

from xml_data import *
from helper import generate_random_string
from helper import generate_room_id
from helper import check_in_conference_time
from helper import get_random_string
from helper import generate_person_id

from Conference import Conference
from Person import Person
from Room import Room
from Event import Event
from Day import Day

def get_conference_parameters():
    '''
    Get the necessary parameters for a conference from user inputs.

    Return title, acronym, start, end, days, timeslot_duration, base_url.
    '''
    acronym_pattern = re.compile('[^a-z0-9_-]')

    title = input("Event title (e.g. Chaos Communication Camp 2019): ")
    acronym = input("Short form of the event (e.g. Camp2019): ")
    acronym = re.sub(acronym_pattern, '', acronym)
    acronym = acronym.lower()
    start, end = None, None

    # Get the conferences start and end date, also calculate the duration in days
    while True:
        start = input("Start of the event (e.g. 2019-08-21): ")
        end = input("Start of the event (e.g. 2019-08-26): ")

        try:
            start = datetime.strptime(start, "%Y-%m-%d")
            end = datetime.strptime(end, "%Y-%m-%d")
        except ValueError:
            print("The format in which you entered the dates isn't valid. Please use: YYYY-MM-DD")
            continue

        days = (end - start).days
        if (end - start).days == 0:
            days = 1
            break
        elif (end - start).days > 0:
            break
        else:
            print("The end of the event is before the start date, please re-enter")
    
    time_pattern = re.compile(r'^\d{2}:\d{2}$')
    timeslot_duration_default = "00:15"
    timeslot_duration = input("Enter the length a timeslot should have (hh:mm). [default=00:15]: ")
    if not timeslot_duration or not time_pattern.match(timeslot_duration): timeslot_duration = timeslot_duration_default
    base_url = input("Enter the base url of your schedule (e.g. https://fahrplan.events.ccc.de/camp/Fahrplan/sched02.html): ")
    
    return title, acronym, start, end, days, timeslot_duration, base_url

def create_conference():
    '''
    Create a Conference object based on parameters that result from a call to 
    get_conference_parameters(). Retrieve the XML from create_conference_xml().

    Return the Conference object.
    '''
    
    title, acronym, start, end, days, timeslot_duration, base_url = get_conference_parameters()
    conference = Conference(title, acronym, start, end, days, timeslot_duration, base_url)
    
    return conference

def get_day_parameters(conference, index):
    '''
    Get the necessary parameters for an day from conference infos.

    Return date, end, start
    '''
    conference_start_date = conference.get_start()
    date = conference_start_date + timedelta(days=(index-1))
    end_date = date + timedelta(days=1)
    start_time = date.strftime("%Y-%m-%dT09:00:00+02:00")
    end_time = end_date.strftime("%Y-%m-%dT04:00:00+02:00")

    return date, end_time, start_time

def create_day(conference, index):
    '''
    Create a Day object based on the conference data.

    Return the Day object.
    '''

    date, end, start = get_day_parameters(conference, index)
    return Day(date, end, index, start)

def create_days(conference):
    '''
    Create all days based on the amount of days of the conference.
    
    Return the created Day objects.
    '''

    days = []
    for i in range(1, conference.get_days()+1):
        days.append(create_day(conference, i))
    return days

def get_room_parameters():
    '''
    Get the necessary parameters for a room from user inputs.

    Return room_name.
    '''
    
    room_name = input("Enter room name: ")
    return room_name

def create_room(conference):
    '''
    Create a Conference object based on parameters that result from a call to 
    get_room_parameters(). Retrieve the XML from create_room_xml().

    Return the Room object.
    '''

    room_name = get_room_parameters()
    room = Room(room_name, conference)
    print(room.get_name())
    return room

def create_rooms(conference):
    '''
    Create a room, than itteratively ask the user if another room should be created.
    
    Return the created Room objects.
    '''

    rooms = []
    room_creation = True

    while room_creation:
        rooms.append(create_room(conference))
        while True:
            new_room_validator = input("Would you like to create another room? (yes/no): ")
            if new_room_validator in ["y", "Y", "yes", "Yes", "true", "True"]:
                break
            elif new_room_validator in ["n", "N", "no", "No", "false", "False"]:
                room_creation = False
                break
    
    return rooms

def get_persons(conference):
    '''
    Get the necessary parameters for a person from user inputs.

    Return person objects in a list.
    '''
    persons = []
    person_creation = True
    while person_creation:
        person_name = input("Enter the sperkers/organizers name/nick: ")
        if not person_name:
            print("Please enter a name")
            continue
        # Check if there already is a person with the entered name
        person = conference.get_person_by_name(person_name)
        if person == None:
            person = Person(conference, person_name, generate_person_id(conference))
            conference.add_person(person)
        else:
            while True:
                print(f"There already is a user named: {person.get_name()}")
                new_person_validator = input("Would you like to change the persons name? (yes/no): ")
                if new_person_validator in ["y", "Y", "yes", "Yes", "true", "True"]:
                    new_person_creation = True
                    break #hier muss man zurück zum anfang der ersten while loop
                elif new_person_validator in ["n", "N", "no", "No", "false", "False"]:
                    new_person_creation = False
                    break
            if new_person_creation:
                continue
        persons.append(person)
        while True:
            new_person_validator = input("Would you like to add another person? (yes/no): ")
            if new_person_validator in ["y", "Y", "yes", "Yes", "true", "True"]:
                break
            elif new_person_validator in ["n", "N", "no", "No", "false", "False"]:
                person_creation = False
                break
    return persons

def get_event_parameters(conference):
    '''
    Get the necessary parameters for an event from user inputs.

    Return guid, eid, date, start, duration, room, slug, url, recording, title, subtitle, track, etype, language, abstract, description, logo, links, attachments.
    '''
    room = None
    while True:
        room = input("Enter the room name in which the event takes place (enter <_rl> for a list of possible rooms): ")
        if room == "_rl":
            print("The following rooms currently exist: ")
            for room_name in conference.get_room_names(): print(room_name)
        elif conference.has_room(room):
            room = conference.get_room_by_name(room)
            break
        else:
            print(f"The room name you entered: {room}, does not exist. Please create the room first.")
            print("If you don't want to cancle the setup now, you may choose an existing room and later change it.")

    guid = generate_random_string()
    eid = generate_room_id(room)
    date, date_format = None, None

    # Get the date events date and time and also check if it's in the time of the conference
    while True:
        date = input("When does the event take place? (e.g. 2019-08-21T11:00:00+02:00): ")
        try:
            date_format = datetime.fromisoformat(date)
            print(date)
        except ValueError:
            print("The format in which you entered the date isn't valid. Please use: date||T||time||timezone")
            continue

        if check_in_conference_time(conference.get_start(), date_format, conference.get_end()):
            break
        else:
            print(f"The entered event date: {date} is before or after the duration of {conference.get_title()}")
    
    start = date_format.time()
    duration = input("Enter the duration of the event (mm:ss or hh:mm:ss): ")
    slug = conference.get_acronym() + "-" + str(conference.get_days()) +  "-" + get_random_string()
    url = input("Enter the events url: ")
    recording = None
    while True:
        recording = input("Is recording allowed?(true/false): ")
        if recording in ["true", "false"]:
            break
        else:
            print("Please specify if recording is allowed or not. Enter 'true' or 'false'")
    title = input("Enter the events title: ")
    subtitle = input("Enter the events subtitle: ")
    track = input("Enter the events track: ")
    etype = input("Enter the events type: ")
    language = input("Entert the events language (e.g. en or de): ")
    abstract = input("Enter events abstract: ")
    description = input("Enter the events description: ")
    logo_opening_tag = "<logo>"
    logo = input("Enter a logo url (e.g. https://www.ccc.de/images/header.png): ")
    if logo:
        logo = logo_opening_tag + logo + "</logo>"
    
    persons = get_persons(conference)    
    links = "" # Only whitespace allowed. I don't know why xD
    attachments = ""
    print("[INFO] You can't enter links and attachments at the moment")
    
    return guid, eid, date, start, duration, room, slug, url, recording, title, subtitle, track, etype, language, abstract, description, logo, persons, links, attachments

def create_event(conference):
    '''
    Create an Event object based on parameters that result from a call to 
    get_event_parameters(). Retrieve the XML from create_event_xml().

    Return the Event object.
    '''

    guid, eid, date, start, duration, room, slug, url, recording, title, subtitle, track, etype, language, abstract, description, logo, persons, links, attachments = get_event_parameters(conference)
    
    event = Event(guid, eid, date, start, duration, room, slug, url, recording, title, subtitle, track, etype, language, abstract, description, logo, persons, links, attachments)
    event.get_id()
    return event

def create_events(conference):
    '''
    Create an event, than itteratively ask the user if another event should be created.
    
    Return the created event objects.
    '''

    events = []
    event_creation = True

    while event_creation:
        events.append(create_event(conference))
        while True:
            new_event_validator = input("Would you like to create another event? (yes/no): ")
            if new_event_validator in ["y", "Y", "yes", "Yes", "true", "True"]:
                break
            elif new_event_validator in ["n", "N", "no", "No", "false", "False"]:
                event_creation = False
                break
    
    return events

def create_schedule_xml(conference):
    schedule_xml = xml_header
    schedule_xml += SCHEDULE_OPENING_TAG
    schedule_xml += SCHEDULE_GENERATOR_FRAB
    schedule_xml += conference.get_conference_xml()
    for day in conference.get_days_obj():
        schedule_xml += day.get_day_xml(conference)
    schedule_xml += SCHEDULE_CLOSING_TAG
    return schedule_xml