class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        self.prev=None

class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
    
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
        if self.is_empty():
            return None #if the stack is empty
        else:
            result=self.tail.value
            self.tail=self.tail.prev
            self.tail.next=None
            #new_head.next=None            
            return result
            

    def push(self, value):
        item=Node(value)
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next=item
            item.prev=self.tail
        self.tail=item


    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tail.value

if "__main__"==__name__:
    test_stack=Stack()
    print (test_stack.size())
    print (test_stack.is_empty())
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(-100)
    print(test_stack.tail)
    while test_stack.size() > 0:
        print(test_stack.pop())
        print(test_stack.pop())
    