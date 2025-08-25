'''We just learn we can make a fuction outside and use it in parent function'''

def mainfunc(func):
    def welcome():
        print("Welcome yo advance Python course")
        func()
        print("please learn these concept properly")
    return welcome()

@mainfunc
def thisis():
    print("this is a advance python course")


'''Decorators are a powerful tool in Python for extending and modifying the behavior of functions and methods.
 They provide a clean and readable way to add functionality such as logging, timing, 
 access control, and more without changing the original code. Understanding and using decorators effectively 
 can significantly enhance your Python programming skills.'''