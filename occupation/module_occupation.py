from datetime import datetime

def extract_data(file_list):
    data = []
    for file_path in file_list:
        with open(file_path, 'r') as file:
            data.append(file.read())
    return data
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