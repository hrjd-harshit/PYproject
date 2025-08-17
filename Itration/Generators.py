# Generators
'''Generators are a simple way to create Iterators. They use the yield keyword to produce a series of 
values lazily which means they generate values on the fly and do not store it in memory.

NOTE : user YIELD Keyword '''

def sqr(n):
    for i in range(n):
        yield i**2
    
for j in sqr(5):
    print(j)

a=sqr(23)
print(next(a))
print(next(a))
print(next(a))

def My_genrator():
    yield 1
    yield 2
    yield 3
    yield 4

print()
gen = My_genrator()
print(next(gen))
print(next(gen))
print(next(gen))
print()
for genz in gen:
    print(genz)


## PRACTICAL EXAMPLE OF GENERATORS
'''GENERATORS ARE PERTICULARY USED TO READ LARGE FILES BECAUSE IT ALLOWS YOU TO PROCESS ONE LINR AT A TIME 
WITHOUT LOADING THE ENTIRE FILE INTO MEMORY.'''

def read_large_file(file_path):
    with open(file_path,'r') as file :
        for line in file:
            yield line

file_path = 'C:\pyproject\Itration\large_file.txt'

bigFile = read_large_file(file_path)
print()
print(next(bigFile))
print(next(bigFile))