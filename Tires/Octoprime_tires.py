from Tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self):
     super().__init__()

    def needs_service(self):
        if(sum(self.tireVal >= 3)):
            return True
        return False