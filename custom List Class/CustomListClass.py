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

    def __len__(self):
        return self.size
    
    def __str__(self):
        output = ""
        for i in range(self.size):
            output = output + str(self.array[i]) + ','
        
        return '[' + output[:-1] + ']'

myList = CustomeList()
myList.append(2)
myList.append(45)
print(len(myList))
myList.append(23)
print(myList)
