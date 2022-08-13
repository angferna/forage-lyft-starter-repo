import unittest
from datetime import date

from Battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_service_true(self):
        battery = SpindlerBattery("2019-09-12", "2022-01-01")
        self.assertTrue(battery.needs_service())

    def test_service_false(self):
        battery = SpindlerBattery("2022-01-02", "2022-01-03")
        self.assertTrue(battery.needs_service())