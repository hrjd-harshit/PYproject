import ctypes

class CustomeList :
    def __init__(self):
        initialCapacity = 1
        self.capacity = initialCapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)
    
    def __create_array(self,capacitiy):
        return(capacitiy*ctypes.py_object)()

    def __resize(self,new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range (self.size):
            new_array[i]=self.array[i]
        
        self.array = new_array ## replace the old array 
        self.capacity = new_capacity 

    def append(self,item):
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)
        
        self.array[self.size] = item
        self.size += 1

    def pop(self):
        if(self.size == 0):
            return ("Pop from empty list")
        
        popped_item = self.array[self.size-1]
        self.size = self.size-1
        return popped_item

    def __len__(self):
        return self.size
    
    def __str__(self):
        output = ""
        for i in range(self.size):
            output = output + str(self.array[i]) + ','
        
        return '[' + output[:-1] + ']'
     
    def __getitem__(self, index):
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index Error: index out of bounds")

    def clear(self):
        self.size=0
        return ("the array is now cleared")

    def insert(self,position,element):
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)        
        
        for index in range(self.size,position,-1):
            self.array[index] = self.array[index-1]

        self.array[position] = element
        self.size += 1

    def remove(self,element):
        for index in range(0,self.size-1):
            if self.array[index] == element:
                newloop = index
                for ind in range(newloop,self.size-1):
                    self.array[ind] = self.array[ind+1]
        self.size -=1
    
myList = CustomeList()
myList.append(2)
myList.append(45)
print(len(myList))
myList.append(23)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop())
print(myList)
myList.append(22)
myList.append(4)
myList.append(23)
print(myList)
myList.insert(2,33)
print()
print(myList)
myList.remove(2)
print(myList)