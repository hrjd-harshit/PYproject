##Encapsulation with getter and setter methord 
## public,protected and private variables or access modifiers

class Person:
    def __init__(self,name,age,place) :
        self.name = name  ## this is a public variable, now the issue is what to do to make this private 
        self.__age = age    ## now here after adding __(++variable name) it becomes private
        ## now we can not access the private variable outside this class or its extended class , no way we can use this.
        
        self._place = place ## now here this is protected variable where we have single _ , 
        ## now we can not access this variable too, from outside the class,
        ## but we can access this from its child class

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else :
            print("Age cannot be nagative")

class Employe(Person):
    def __init__(self, name, age, place):
        super().__init__(name, age, place)


    
person = Person("hatshit",23,"Pune")
person.set_age(56)
age = person.get_age()
print(age)
