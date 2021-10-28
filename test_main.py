import unittest
from main import get_name
from main import get_date


class test(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(get_name(), 'Alex')  # input Alex
        self.assertEqual(get_name(), 'Maxim')  # input Maxim
        self.assertEqual(get_name(), 'Anton')  # input Anton

    def test_get_date(self):
        self.assertEqual(get_date(), "28/10/2021 13:40:10")