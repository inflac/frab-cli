from datetime import datetime

import secrets
import string
import pytz  # For timezone handling
import uuid
import os

def check_path_exists(path:str, create=False):
    '''
    Check wether path exists or not.
    If path do not exist but create=True,
    create a directory.
    '''
    path_exist = os.path.exists(path)
    if path_exist:
        return True

    #path do not exist, try to create it
    if create:
        try:
            os.makedirs(path)
            return True
        except OSError as e:
            print(f"Failed to create directory: {path}")
            print(f"Error: {e}")
            return False
    return False

def generate_random_string(length=8):
    guid = uuid.uuid4()
    return str(guid)

def generate_id(room):
    highest_id = 0
    for event in room.get_events():
        if event.get_id() > highest_id: highest_id = event.get_id()
    return (highest_id + 1)

def check_in_conference_time(start_date, to_check, end_date):    
    local_timezone = pytz.timezone('Europe/Berlin')  # Adjust timezone as per your requirements
    start_date = local_timezone.localize(start_date)
    end_date = local_timezone.localize(end_date)

    # In the conference start and end were set to the same date, an event's time
    # should be valid if it's on the conferences date
    if start_date == end_date and start_date.year == to_check.year and start_date.month == to_check.month and start_date.day == to_check.day:
        return True
    else:
        return start_date <= to_check <= end_date

def get_random_string():
    random_string = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    return random_string