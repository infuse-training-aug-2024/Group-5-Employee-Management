import unittest
import os
import tempfile
import numpy as np
from performance import Performance


class TestPerformance(unittest.TestCase):

    def setUp(self):
        self.performance = Performance(
            employee_id=1,
            behaviour=8,
            team_collaboration=7,
            verbal_skills=9,
            critical_thinking=6,
            emotional_intelligence=8
        )
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_file.close()

    def tearDown(self):
        # Remove the temporary file after the test
        os.remove(self.temp_file.name)

    def test_get_performance_avg(self):
        self.performance.get_performance_avg()
        expected_avg = (8 + 7 + 9 + 6 + 8) / 5
        self.assertEqual(self.performance.average, expected_avg)

    def test_save_to_csv_new_employee(self):
        # Ensure the file is empty
        with open(self.temp_file.name, 'w') as f:
            f.write('')

        # Save to CSV
        self.performance.save_to_csv(self.temp_file.name)

        # Verify that the file now contains the correct data
        data = np.genfromtxt(self.temp_file.name, delimiter=',', dtype=None, names=True, encoding=None)

        # Check if the data is correct
        self.assertEqual(data['employee_id'], 1)
        self.assertEqual(data['behaviour'], 8)
        self.assertEqual(data['team_collaboration'], 7)
        self.assertEqual(data['verbal_skills'], 9)
        self.assertEqual(data['critical_thinking'], 6)
        self.assertEqual(data['emotional_intelligence'], 8)
        self.assertAlmostEqual(data['average'], (8 + 7 + 9 + 6 + 8) / 5)

    def test_save_to_csv_existing_employee(self):
        # Prepare initial data with one employee
        initial_data = np.array([(1, 5, 6, 7, 8, 9, 7.0)],
                                dtype=[('employee_id', 'i4'), ('behaviour', 'i4'), 
                                       ('team_collaboration', 'i4'), ('verbal_skills', 'i4'), 
                                       ('critical_thinking', 'i4'), ('emotional_intelligence', 'i4'), 
                                       ('average', 'f4')])
        # Save initial data to the temp file
        np.savetxt(self.temp_file.name, initial_data, delimiter=',', fmt='%d,%d,%d,%d,%d,%d,%f',
                   header=','.join(initial_data.dtype.names), comments='')

        # Save the updated performance to the same file
        self.performance.save_to_csv(self.temp_file.name)

        # Verify that the file now contains the updated data
        data = np.genfromtxt(self.temp_file.name, delimiter=',', dtype=None, names=True, encoding=None)

        # Check if the data is updated correctly
        self.assertEqual(data['employee_id'], 1)
        self.assertEqual(data['behaviour'], 8)
        self.assertEqual(data['team_collaboration'], 7)
        self.assertEqual(data['verbal_skills'], 9)
        self.assertEqual(data['critical_thinking'], 6)
        self.assertEqual(data['emotional_intelligence'], 8)
        self.assertAlmostEqual(data['average'], (8 + 7 + 9 + 6 + 8) / 5)

if __name__ == '__main__':
    unittest.main()
