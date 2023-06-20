from abc import ABC

from tire.tire import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        sum = 0
        for x in self.wear_sensors:
            if x >= 0.9:
                return True
        return False