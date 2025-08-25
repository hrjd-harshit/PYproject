''' Decorators are a powerful and flexible feature in python that allows you to modify the behavior of a functionor class methord, they are commonly user to add functionality to 
functions or methord without modifing there actual code this lesson coverse the basics of Decorators, including how to create and use them.'''


## function copy 

def firstone():
    print("this is the first function")
    return "this is the first function"

secondone = firstone
print(secondone())
secondone()

## what if we will detete firstone function it was the orignal one ??

del firstone # we have deleted the orignal one 
firstone() ## if we are runing this code it is telling us function not define

# lets call the another one
secondone() ## it is still running.