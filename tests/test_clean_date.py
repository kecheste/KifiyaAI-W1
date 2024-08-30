import unittest
from scripts.helper import clean_date

class TestCleanDate(unittest.TestCase):

    def test_clean_date_with_timezone(self):
        result = clean_date("2024-08-30T15:00:00+02:00")
        self.assertEqual(result, "2024-08-30T15:00:00")

    def test_clean_date_without_timezone(self):
        result = clean_date("2024-08-30T15:00:00")
        self.assertEqual(result, "2024-08-30T15:00:00")

    def test_clean_date_with_invalid_input(self):
        result = clean_date(20240830)
        self.assertEqual(result, 20240830)

    def test_clean_date_with_empty_string(self):
        result = clean_date("")
        self.assertEqual(result, "")

    def test_clean_date_with_none(self):
        result = clean_date(None)
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
