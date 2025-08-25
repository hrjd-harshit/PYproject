## closures function 

def main():
    mdg = "welcome" # we can user this variable in any sub methord we want 
    def sub_welcome_methord():
        print ("welcome to the advance python cource")
        print(mdg)
        print("please learn it with full focus")

    return sub_welcome_methord() ## a sub methord can be user as return tupe to parent methord 
         
main()

'''Can we use variable of parent class as return type ? ---- > yes this can be done such an stupid question'''
'''Can child def have return value but not the parent def ?? -----> nope will not work we need to have return type for a function'''

def mainn():
    mdg = "welcome"
    def sub_welcome_methord(): #this can only be called inside this function
        print ("welcome to the advance python cource")
        print(mdg)
        print("please learn it with full focus")
        return mdg

print()
print(mainn())

'''See what esle we can do is we can pass a function as an argument in a function,in below example we just told them an internal methord to be called '''

def mainFun(newfunc):
    def childFun():
        print("something")
        newfunc("print")
        print("something again")
    return childFun()

mainFun(print)
print("-----------")

def LenLst(met,lst):
    def lenn():
        print(met(lst))
    return lenn()

LenLst(len,[1,2,3,4,5])