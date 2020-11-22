class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        self.prev=None

class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def get_head(self):
        if self.head is None:
            return None
        else:
            return self.head.value
    
    def get_tail(self):
        if self.tail is None:
            return None
        else:
            return self.tail.value
    
    def size(self):
        node = self.head
        length=0
        while node is not None:
            length+=1
            node = node.next
        return length  
    
    def is_empty(self):
        if self.size()==0:
            return True
        else:
            return False

    
    def pop(self):
        if self.head is None:
            return None #if the stack is empty
        else:
            if self.head.next is None: #case from one item
                item=self.head
                self.head=None
                self.tail=None
            else: 
                item=self.tail
                self.tail=item.prev
                if self.tail:
                    self.tail.next=None #case from two items                              
            return item.value           
   

    def push(self, value):
        item=Node(value)
        if self.head is None:
            self.head = item         
            
        else:
            self.tail.next=item
            item.prev=self.tail          
        self.tail=item

    

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.tail.value

    