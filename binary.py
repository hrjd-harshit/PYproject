def binary(a,tg,start,endd):
    leng = len(a)
    start = 0
    mid = (leng-start)//2
    if a[mid] == tg:
        return mid
    elif a[mid]< tg :
        start = mid +1
        binary(a,tg) 
    else :
        leng = mid-1
        binary(a,tg)

def sort (a):
    size = len(a)
    support = 0
    for i in range(0,size):
        for j in range(i,size):
            if a[i]>a[j] :
                support = a[i]
                a[i] = a[j]
                a[j] = support
    return a

lstt = [23,2,11,5,6]
my_data = sort(lstt)
tg =11
print (my_data)
print (binary(my_data,tg))