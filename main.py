from pathlib import Path
import argparse

from schedule_methods import create_schedule

def main(create:bool):
    if create: create_schedule()
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='python main.py', description='Script for schedule creation on the commandline in frab format', epilog='')
    parser.add_argument('-c', '--create', action='store_true', help='create a new schedule')

    args = parser.parse_args()
    create = args.create

    main(create)
