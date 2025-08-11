class Animal : 
    def speak(self):
        return "sound of the animal"

class dog(Animal):
    def speak(self):
        return "woff"

class cat(Animal):
    def speak(self):
        return "meow"

## independent function

def animal_speek(animal):
    print(animal.speak())

Dog = dog()
Cat = cat()
animal = Animal()
print(animal.speak())
print(Dog.speak())
print(Cat.speak())
animal_speek(Cat)