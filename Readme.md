# frab-cli
frab-cli is a commandline tool for schedule creation in [frab](https://github.com/frab) format. Simply enter the schedule informations from the commandline and generate a .xml schedule.

## Notes
Please be aware about frab-clis unfinished codebase. Currently there is no support for persons.

## Usage
```
usage: python main.py [-h] [-c]

Script for schedule creation on the commandline in frab format

options:
  -h, --help    show this help message and exit
  -c, --create  create a new schedule
```

## Verification
Because frab-cli isn't finished yet you can check the correctness of the generated schedule with the provided script `validate_schedule_xml.sh`. The script was written by the [VOC](https://github.com/voc/schedule/tree/master/validator/xsd).
You can also use this [online validator](https://c3voc.de/schedulexml/).