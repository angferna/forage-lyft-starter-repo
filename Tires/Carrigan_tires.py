from Tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self):
     super().__init__()

    def needs_service(self):
        for val in self.tireVal:
            if val >= 0.9:
                return True
        return False