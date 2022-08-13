import unittest
from Tires.Carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
        
    def test_carriganTire_should_serviced(self):
        tireVal = [0.9, 0.2, 0.3, 0]
        carriganTires = CarriganTires(tireVal)
        self.assertTrue(carriganTires.needs_service())

    def test_carriganTires_should_not_serviced(self):
        tireVal = [0, 0, 0, 0]
        carriganTires = CarriganTires(tireVal)
        self.assertFalse(carriganTires.needs_service())