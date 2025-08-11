from abc import ABC,abstractmethod

## Abstract base class 
class Vehical(ABC):
    def drive(self):
        print("this vehical is used for driving")
    
    @abstractmethod
    def start_engine(self):
        pass

class car(Vehical):
    def start_engine(self):
        print("this Engine is working")
    

def operate_vehical(vehical):
    vehical.start_engine()
    vehical.drive()

Car = car()
operate_vehical(Car)