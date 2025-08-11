def lenearSearch(arr,target) : 
    size  = len(arr)
    for i in range(1,size):
        if arr[i] == target :
            return i 
        
    return -1

Lsttt = [1,2,3,0,54]
target = 54
result = lenearSearch(Lsttt,target)
if result == 0 :
    print("target not found")
else : 
    print(result)