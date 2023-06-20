import unittest

from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class TestOctoprimeTire(unittest.TestCase):

    def test_tire_should_not_be_serviced(self):
        wear_sensors = [0.1, 0.2, 0.3, 0.4]
        tires = OctoprimeTire(wear_sensors)
        self.assertFalse(tires.needs_service())

    def test_tire_should_be_serviced(self):
        wear_sensors = [0.9, 0.8, 0.7, 0.9]
        tires = OctoprimeTire(wear_sensors)
        self.assertTrue(tires.needs_service())

class TestCarriganTire(unittest.TestCase):

    def test_tire_should_not_be_serviced(self):
        wear_sensors = [0.1, 0.2, 0.3, 0.4]
        tires = CarriganTire(wear_sensors)
        self.assertFalse(tires.needs_service())

    def test_tire_should_be_serviced(self):
        wear_sensors = [0.1, 0.2, 0.3, 0.9]
        tires = CarriganTire(wear_sensors)
        self.assertTrue(tires.needs_service())