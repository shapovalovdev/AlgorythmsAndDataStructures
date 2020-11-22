class Node:
    def __init__(self,v):
        self.next=None
        self.prev=None
        self.value=v
class Deque:
    def __init__(self):
        self.front=None
        self.tail=None

    def addFront(self, item):
        node=Node(item)
        if self.front is None:   #case of none items         
            self.front=node
            self.tail=node
        elif self.tail is self.front: # case of 1 item
            self.tail.prev=node
            self.front=node
            node.next=self.tail
        else: # case of several items
            self.front.prev=node
            prev_front=self.front
            self.front=node
            node.next=prev_front       
            

    def addTail(self, item):
        node=Node(item)
        if self.front is None:
            self.front = node           
        else:
            self.tail.next=node
            node.prev=self.tail          
        self.tail=node

    def removeFront(self):
        if self.front is None:
            return None #if the stack is empty
        else:
            item=self.front
            if self.front.next is not None:                
                self.front=self.front.next
            elif self.front.next is self.tail:
                self.front=self.tail
            else:
                self.front=None
                self.tail=None
            return item.value   

    def removeTail(self):
        if self.front is None:
            return None #if the stack is empty
        else:
            if self.front.next is None: #case from one item
                item=self.front
                self.front=None
                self.tail=None
            else: 
                item=self.tail
                self.tail=item.prev
                item.prev.next=None #case from two items                              
            return item.value     

    def size(self):
        node = self.front
        length=0
        while node is not None:
            length+=1
            node = node.next
        return length
    
    def getFront(self):
        if self.front is None:
            return None
        else:
            return self.front.value
    
    def getTail(self):
        if self.tail is None:
            return None
        else:
            return self.tail.value