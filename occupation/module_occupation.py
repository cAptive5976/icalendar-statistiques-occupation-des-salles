from datetime import datetime

def extract_data(file_list):
    data = []
    for file_path in file_list:
        with open(file_path, 'r') as file:
            data.append(file.read())
    return data

def process_data(data):
    processed_data = []

    for ics_content in data:
        lines = ics_content.split('\n') 
        events = []  
        current_event = None 

        for line in lines:  
            if line.startswith('BEGIN:VEVENT'):
                current_event = {} 
            elif line.startswith('SUMMARY:'):  
                current_event['summary'] = line.split(':')[-1]
            elif line.startswith('LOCATION:'):  
                current_event['location'] = line.split(':')[-1]
            elif line.startswith('DESCRIPTION:'): 
                description_parts = line.split('\n')
                current_event['group'] = description_parts[1].strip()  
                current_event['teacher'] = description_parts[2].strip()  
            elif line.startswith('DTSTART:'):  
                start_time = line.split(':')[-1]
                current_event['start_time'] = datetime.strptime(start_time, '%Y%m%dT%H%M%S').strftime('%d-%m-%Y %H:%M')
            elif line.startswith('DTEND:'): 
                end_time = line.split(':')[-1]
                current_event['end_time'] = datetime.strptime(end_time, '%Y%m%dT%H%M%S').strftime('%d-%m-%Y %H:%M')
            elif line.startswith('END:VEVENT'): 
                events.append(current_event)

        processed_data.extend([event for event in events if event.get('summary', '')])

    return processed_data

def generate_html(data, output_dir):
    html_content = """
    <html>
    <body>
        <table border="1">
            <tr>
                <th>Salle</th>
                <th>Heures d’utilisation moyen/semaine</th>
                <th>Heures d’utilisation moyen/jour    </th>
                <th>Taux d’occupation (%)</th>
            </tr>
    """

    for event in data:
        html_content += f"""
            <tr>
                <td>{event['start_time']}</td>
                <td>{event['end_time']}</td>
                <td>{event.get('summary', '')}</td>
                <td>{event.get('location', '')}</td>
                <td>{event.get('group', '')}</td>
                <td>{event.get('teacher', '')}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_dir + 'index.html', 'w') as file:
        file.write(html_content)