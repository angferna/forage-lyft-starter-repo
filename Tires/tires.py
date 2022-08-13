from abc import ABC

class Tires(ABC):
    def __init__(self, tireVal):
        self.tireVal = tireVal

    def needs_service(self):
        pass
