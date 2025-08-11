def selection(lst):
    lenn = len(lst)
    for j in range(lenn-1):
        min_index = j
        for i in range(j+1,lenn):
            if lst[i]<lst[min_index] :
                min_index = i
        lst[j],lst[min_index] = lst[min_index],lst[j]
    return lst
lst = [1,12,23,45,6,78,44,13]
print (selection(lst))