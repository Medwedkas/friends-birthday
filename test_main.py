import unittest
from main import obj


class test(unittest.TestCase):
    def test_get_person(self):
        self.assertEqual(obj.get_person(), 'Alex')  # input Alex
        self.assertEqual(obj.get_person(), 'Maxim')  # input Maxim
        self.assertEqual(obj.get_person(), 'Anton')  # input Anton

    def test_get_date(self):
        self.assertEqual(obj.get_date(), 60.0)  # input 1
        self.assertEqual(obj.get_date(), 120.0)  # input 2
