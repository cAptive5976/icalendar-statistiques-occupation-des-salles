import unittest
import os
from occupation import module_occupation
from datetime import datetime

class TestOccupation(unittest.TestCase):
    def test_extract_data(self):
        calendar_1_path = 'tests/sorties/test_ADECal_BUT1.ics'
        calendar_2_path = 'tests/sorties/test_ADECal_BUT2.ics'
        with open(calendar_1_path, 'w') as calendar_1:
            calendar_1.write('BEGIN:VEVENT\nSUMMARY:Cours 1\nLOCATION:Salle RT04\nDTSTART:20220101T120000Z\nDTEND:20220101T130000Z\nEND:VEVENT')
        with open(calendar_2_path, 'w') as calendar_2:
            calendar_2.write("BEGIN:VEVENT\nSUMMARY:Cours 2\nLOCATION:Salle RT05\nDTSTART:20220102T120000Z\nDTEND:20220102T130000Z\nEND:VEVENT")
        liste_calendar = [calendar_1_path, calendar_2_path]
        result = module_occupation.extract_data(liste_calendar)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'BEGIN:VEVENT\nSUMMARY:Cours 1\nLOCATION:Salle RT04\nDTSTART:20220101T120000Z\nDTEND:20220101T130000Z\nEND:VEVENT')
        self.assertEqual(result[1], 'BEGIN:VEVENT\nSUMMARY:Cours 2\nLOCATION:Salle RT05\nDTSTART:20220102T120000Z\nDTEND:20220102T130000Z\nEND:VEVENT')
    def test_process_data(self):
        data = ["BEGIN:VEVENT\nSUMMARY:Cours 1\nLOCATION:Salle RT04\nDTSTART:20220101T120000Z\nDTEND:20220101T130000Z\nEND:VEVENT",
                "BEGIN:VEVENT\nSUMMARY:Cours 2\nLOCATION:Salle RT05\nDTSTART:20220102T120000Z\nDTEND:20220102T130000Z\nEND:VEVENT"]
        processed_data = module_occupation.process_data(data)
        self.assertEqual(len(processed_data), 2)
        self.assertEqual(processed_data[0]['summary'], 'Cours 1')
        self.assertEqual(processed_data[1]['summary'], 'Cours 2')

    def test_generate_html(self):
        data = [{"location": "RT04 [I04]", "start_time": datetime(2022, 1, 1, 12, 0), "end_time": datetime(2022, 1, 1, 13, 0)},
                {"location": "RT05 [I04]", "start_time": datetime(2022, 1, 2, 12, 0), "end_time": datetime(2022, 1, 2, 13, 0)}]
        output_dir = 'tests/sorties/html/'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        module_occupation.generate_html(data, output_dir)
        html_file_path = os.path.join(output_dir, 'index.html')
        self.assertTrue(os.path.exists(html_file_path))
        

if __name__ == '__main__':
    unittest.main()