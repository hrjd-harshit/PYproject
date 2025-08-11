def bubble_sort(arr):
        leng = len(arr)
        box = 0
        count = 0
        while (leng !=0):
            for i in range(0,leng-1):
                if(arr[i]>arr[i+1]):
                    box = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = box
                count = count+1
            leng = leng-1
        return arr   

set_of = [1,12,23,45,6,78,44,13]
new_set = bubble_sort(set_of)
print(new_set)