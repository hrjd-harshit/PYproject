def selactionsort(lst):
    size = len(lst)

    for i in range(0,size):
        current_val = lst[i]
        correct_position = i-1
        while correct_position>=0 :
            if(lst[correct_position]<current_val):
                break
            else :
                lst[correct_position+1] = lst[correct_position]
                correct_position-=1
            
            lst[correct_position+1] = current_val
    
    return lst


list = [21,44,3,11,11,17,2]
print (selactionsort(list))