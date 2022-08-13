from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self):
        super()

    @abstractmethod
    def needs_service(self):
        pass
