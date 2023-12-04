import argparse
import datetime

def parse_ics_file(filename):
    events = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.startswith('BEGIN:VEVENT'):
                event = {}
                for key, value in line.split(':'):
                    event[key] = value.strip()
                events.append(event)
    return events