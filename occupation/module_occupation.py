import argparse
import datetime

def importation(fichier):
    with open(fichier, 'r') as f:
        calendar = f.read()
    events = []
    for event in calendar.split('BEGIN:VEVENT'):
        summary = event.split('SUMMARY:')[1].split('\n')[0]
        description = event.split('DESCRIPTION:')[1].split('\n')[0]
        start = datetime.datetime.strptime(event.split('DTSTART:')[1].split('\n')[0], '%Y-%m-%dT%H:%M:%S')
        end = datetime.datetime.strptime(event.split('DTEND:')[1].split('\n')[0], '%Y-%m-%dT%H:%M:%S')
        location = event.split('LOCATION:')[1].split('\n')[0]
        organizer = event.split('ORGANIZER;CN=')[1].split(':')[0]
        attendees = [a.split('ATTENDEE;CN=')[1].split(':')[0] for a in event.split('ATTENDEE;CN=')[1:]]
        events.append({
            'summary': summary,
            'description': description,
            'start': start,
            'end': end,
            'location': location,
            'organizer': organizer,
            'attendees': attendees
        })

    return events

fichiers = ['../data/ADECal_BUT1.ics', '../data/ADECal_BUT2.ics', '../data/ADECal_BUT3.ics']

for fichier in fichiers:
    events = importation(fichier)
    print(events)

    

#création d'une variable pour y entrer les données

#définition du début et de la fin de ce qu'il faut lire

#définition des éléments à garder (heure, salle)

#association des données avec leurs correspondances

