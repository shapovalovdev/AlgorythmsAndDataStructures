from src.Stack.stack_linked_list import Stack
from src.Stack.stack_linked_list_head import StackHead

class DequeStacks(Stack,StackHead):
    def __init__(self):
        Stack.__init__(self)
    
    def addFront(self, item):
        StackHead.push(self,item)
    
    def addTail(self, item):
        Stack.push(self,item)
    
    def removeFront(self):
        return StackHead.pop(self)

    def removeTail(self):
        return Stack.pop(self)

    def getFront(self):
        return Stack.get_head(self)

    def getTail(self):
        return Stack.get_tail(self)
    
    def size(self):
        return Stack.size(self)