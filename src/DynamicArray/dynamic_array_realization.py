import ctypes

class DynArray:
    _MIN_CAPACITY=16
    def __init__(self):
        self.count = 0
        self.capacity = self._MIN_CAPACITY
        self.array=self.make_capacity(self.capacity)
    
    def __len__(self):
        return self.count
    
    def make_capacity(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]
    
    def resize(self, new_capacity):
        new_array=self.make_capacity(new_capacity)
        for i in range(self.count):
            new_array[i]=self.array[i]
        self.array=new_array
        self.capacity=new_capacity
    
    def append(self,itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count]=itm
        self.count+=1
    
    def insert(self,i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        
        for j in range(self.count,i,-1):
            self.array[j]=self.array[j-1]            
        self.array[i]=itm
        self.count+=1    
    
    
    def delete(self,i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        self.count-=1
        for j in range(i,self.count):
            self.array[j]=self.array[j+1]
        def shrink():
            if self.capacity==self._MIN_CAPACITY:
                return
            current_occupancy=self.count/self.capacity
            threshold=0.5
            shrink_to=int(self.capacity/1.5)     
            if current_occupancy < threshold:                       
                if shrink_to <= self._MIN_CAPACITY:
                    self.resize(self._MIN_CAPACITY)
                else:
                    self.resize(shrink_to)    
        shrink()          


        

