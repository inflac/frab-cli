
import os

from xml_data import *
from helper import check_path_exists
from schedule_creator_helper import create_conference, create_days, create_rooms, create_events
from schedule_creator_helper import create_schedule_xml

def create_schedule():
    path = None
    while True:
        path = input("Where to store the schedule? Input a path: ")
        if check_path_exists(path):
            break
        else:
            print("Path wasn't valid and may already exist.")
    
    # Create Conference
    print("### Conference creation ###")
    conference = create_conference()
    print("### Conference creation done ###")
    # Create Days
    print("### Day creation ###")
    days_obj = create_days(conference)
    conference.set_days_obj(days_obj)
    print("### Day creation done ###")
    # Create Rooms
    print("### Room creation ###")
    rooms = create_rooms(conference)
    conference.set_rooms(rooms)
    print("### Room creation done ###")
    # Create Events for every conference day
    for i,day in enumerate(days_obj):
        print(f"### Day {i} - Event creation ###")
        events = create_events(conference)
        day.set_events(events)
        print(f"### Day {i} - Event creation done ###")
    print("### Schedule creation done ###")
    
    schedule_xml = create_schedule_xml(conference)
    with open(os.path.join(path, "schedule.xml"), "w+") as f:
        f.write(schedule_xml)
    
    