"""Queue implementation with help of stacks"""
from src.Stack.stack_linked_list import Stack
from src.Stack.stack_linked_list_head import StackHead
class Node:
    def __init__(self,v):
        self.next=None
        self.value=v
class QueueStacks:
    def __init__(self):
        Stack.__init__(self) #initialize with stack end
    
    def enqueue(self, item): #need to add element to the end of the list
        Stack.push(self, item)
    
    def dequeue(self): #need to remove element from the beginning of the list
        return StackHead.pop(self)
    
    def size(self):
        return Stack.size(self)
    
    def get_head(self):
        return Stack.get_head(self)
    
    def get_tail(self):
        return Stack.get_tail(self)    

    


