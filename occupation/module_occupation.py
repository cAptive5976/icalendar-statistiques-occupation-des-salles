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
            elif line.startswith('DTSTART:'):  
                start_time = line.split(':')[-1]
                current_event['start_time'] = datetime.strptime(start_time, '%Y%m%dT%H%M%SZ')
            elif line.startswith('DTEND:'):
                end_time = line.split(':')[-1]
                current_event['end_time'] = datetime.strptime(end_time, '%Y%m%dT%H%M%SZ')
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
                <th>Heures d'utlisation</th>
                <th>Heures d’utilisation moyen/semaine</th>
                <th>Heures d’utilisation moyen/jour</th>
                <th>Taux d’occupation (%)</th>
            </tr>
    """

    for event in data:
        location = event['location']
        total_hours = sum((event['end_time'] - event['start_time']).total_seconds() / 3600 for event in data if event['location'] == location)
        html_content += f"""    
            <tr>
                <td>{location}</td>
                <td>{total_hours}</td>
                <td>{total_hours / len(data)}</td>
                <td>{total_hours / 7}</td>
                <td>{total_hours / len(data) * 100}%</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_dir + 'index.html', 'w') as file:
        file.write(html_content)