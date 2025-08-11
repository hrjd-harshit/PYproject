def sort (a):
    size = len(a)
    support = 0
    count = 0
    for i in range(0,size):
        for j in range(i,size):
            if a[i]>a[j] :
                support = a[i]
                a[i] = a[j]
                a[j] = support
            count = count+1  
        print (count)
    return a

lstt = [1,12,23,45,6,78,44,13]
print (sort(lstt))