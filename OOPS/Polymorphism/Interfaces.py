## polymorphism with Abstract Base class 

from abc import ABC,abstractmethod

## defining an abstract class 
class vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## drive class 1 
class car(vehical):
    def start_engine(self):
        return "car engine is Started"

class motercycle(vehical):
    def start_engine(self):
        return "Motercycle Engine is started"

def start_vehical(Vehical):
    print(Vehical.start_engine())

## making object for the class 

Car = car()
Motercycle = motercycle()

start_vehical(Motercycle)