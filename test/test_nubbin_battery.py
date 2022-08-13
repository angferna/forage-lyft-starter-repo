import unittest
from datetime import date

from Battery.NubbinBattery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_service_true(self):
        battery = NubbinBattery("2019-09-12", "2022-01-01")
        self.assertTrue(battery.needs_service())

    def test_service_false(self):
        battery = NubbinBattery("2022-01-02", "2022-01-03")
        self.assertTrue(battery.needs_service())