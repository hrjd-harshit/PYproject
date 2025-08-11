### Inheritence
### Parant class 

class car :
    def __init__(self,windows,gates,EnginType,):
        self.windows = windows
        self.gates = gates
        self.EnginType = EnginType

    def drive(self):
        print(f'the person will drive the {self.EnginType} car')

### this is the child class which inharets the parent class

class EV_Car(car):
    def __init__(self, windows, gates, EnginType,is_selfDriving):
        super().__init__(windows, gates, EnginType)
        self.is_selfDriving = is_selfDriving
    
    def selfDriving(self):
        print(f"tesela is a {self.EnginType} car hence is an EV {self.is_selfDriving} and this statment is true")

tesla1 = EV_Car(4,4,"Electrical",True)

tesla1.selfDriving()
tesla1.drive()