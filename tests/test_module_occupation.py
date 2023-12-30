import unittest
import os
from occupation import module_occupation
from datetime import datetime

class TestOccupation(unittest.TestCase):
    def test_extract_data(self):
        calendar_1_path = 'test_ADECal_BUT1.ics'
        calendar_2_path = 'test_ADECal_BUT2.ics'
        with open(calendar_1_path, 'w') as calendar_1:
            calendar_1.write('Calendrier BUT1')
        with open(calendar_2_path, 'w') as calendar_2:
            calendar_2.write("Calendrier BUT2")
        liste_calendar = [calendar_1_path, calendar_2_path]
        result = module_occupation.extract_data(liste_calendar)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'Calendrier BUT1')
        self.assertEqual(result[1], 'Calendrier BUT2')
        os.remove('test_ADECal_BUT2.ics')
        os.remove('test_ADECal_BUT1.ics')
    def test_process_data(self):
        data = ["BEGIN:VEVENT\nSUMMARY:Event 1\nLOCATION:Room A\nDTSTART:20220101T120000Z\nDTEND:20220101T130000Z\nEND:VEVENT",
                "BEGIN:VEVENT\nSUMMARY:Event 2\nLOCATION:Room B\nDTSTART:20220102T120000Z\nDTEND:20220102T130000Z\nEND:VEVENT"]
        processed_data = module_occupation.process_data(data)
        self.assertEqual(len(processed_data), 2)
        self.assertEqual(processed_data[0]['summary'], 'Event 1')
        self.assertEqual(processed_data[1]['summary'], 'Event 2')

    def test_generate_html(self):
        data = [{"location": "Room A", "start_time": datetime(2022, 1, 1, 12, 0), "end_time": datetime(2022, 1, 1, 13, 0)},
                {"location": "Room B", "start_time": datetime(2022, 1, 2, 12, 0), "end_time": datetime(2022, 1, 2, 13, 0)}]
        output_dir = 'output/'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        module_occupation.generate_html(data, output_dir)
        html_file_path = os.path.join(output_dir, 'index.html')
        self.assertTrue(os.path.exists(html_file_path))
        os.remove(html_file_path)
        os.rmdir(output_dir)
        

if __name__ == '__main__':
    unittest.main()