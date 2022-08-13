from abc import ABC

from Battery import Battery


class SplinderBattery(battery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.last_service_date = current_mileage
        self.current_date = last_service_mileage

    def needs_service(self):
        days = self.current_date - self.last_service_date
        if(days>= 365*3):
            return True
        return False
