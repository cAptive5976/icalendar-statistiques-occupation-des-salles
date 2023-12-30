import unittest
from occupation import module_occupation

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

if __name__ == '__main__':
    unittest.main()