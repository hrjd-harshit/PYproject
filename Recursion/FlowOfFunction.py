def printNoNum(num):
    print(num)
    if num != 0 :
        num = num-1
        printNoNum(num)

printNoNum(6)

'''Let us understand few concept on function '''
'''1. we can call  a function from inside for another function '''
'''2. A Function stayes in the memory until it gets fully exucuted '''

"DRY principal Do not repet yourself "

"yes a function calles himself "