from unittest import TestCase

from src.solarcalendar.main import *


class IsLeapTestCase(TestCase):
    """test isleap function"""

    def test_isleap_for_leap_year(self):
        result = isleap(1399)
        self.assertTrue(result)

    def test_isleap_for_non_leap_year(self):
        result = isleap(1400)
        self.assertFalse(result)

    def test_is_leap_for_before_1343(self):
        result = isleap(1321)
        self.assertTrue(result)

    def test_is_non_leap_for_before_1343(self):
        result = isleap(1320)
        self.assertFalse(result)


class LeapdaysTestCase(TestCase):
    """test leapdays function"""

    def test_with_correctly_parameter(self):
        result = leapdays(1397, 1404)
        self.assertEqual(result, 2)

    def test_first_year_greater_than_second(self):
        with self.assertRaises(AssertionError):
            leapdays(1400, 1399)


class WeekDayTestCase(TestCase):
    """test weekday function"""

    def test_with_correct_parameter(self):
        """Farvardin 1, 1400 is saturday"""
        self.assertEqual(weekday(1400, 1, 1), 1)

    def test_with_unsupported_year(self):
        with self.assertRaises(AssertionError):
            weekday(-1400, 1, 1)


class MonthRangeTestCase(TestCase):
    """test mongthrange function"""

    def test_with_correct_parameter(self):
        self.assertEqual((1, 31), monthrange(1400, 1))

    def test_for_esfand_of_non_leap_year(self):
        self.assertEqual((1, 29), monthrange(1400, 12))

    def test_for_esfand_of_leap_year(self):
        self.assertEqual((6, 30), monthrange(1399, 12))
