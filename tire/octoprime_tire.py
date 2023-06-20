from abc import ABC

from tire.tire import Tire


class OctoprimeTire(Tire, ABC):
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self):
        sum = 0
        for x in self.wear_sensors:
            sum += x
        if sum >= 3:
            return True
        else:
            return False
