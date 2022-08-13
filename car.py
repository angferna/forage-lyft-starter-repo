from abc import ABC, abstractmethod
from Engine import engine
from Battery import battery


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = engine 
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
