class dog : 
    def __init__(self,name,age,speed):
        self.name =name
        self.age=age
        self.speed = speed
    def run(self):
        print(f'{self.name} runs at a speed of {self.speed} km per hr at age of {self.age}')
dog1 = dog("sharu",4,44)
print(dog1.name)
print(dog1.age)
print(dog1.run())