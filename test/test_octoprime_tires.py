import unittest
from Tires.Octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):     
    
    def test_octoprimeTires_should_serviced(self, tireVal):
        tireVal = [1.3, 0, 1.1, 1.8]
        octoprimeTires = OctoprimeTires(tireVal)
        self.assertTrue(octoprimeTires.needs_service())

    def test_octoprimeTires_should_not_serviced(self, tireVal):
        tireVal = [0, 0, 0, 1]
        octoprimeTires = OctoprimeTires(tireVal)
        self.assertFalse(octoprimeTires.needs_service())