class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        self.prev=None
        

class StackHead:
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
        if self.head is None:
            return None #if the stack is empty
        else:
            item=self.head
            if self.head.next is not None:                
                self.head=self.head.next
            elif self.head.next is self.tail:
                self.head=self.tail                      
            else:
                self.head=None
                self.tail=None
            return item.value            

    def push(self, value):
        item=Node(value)
        if self.head is None:
            self.head=item
            self.tail=item
        elif self.tail is self.head: # case of 1 item
            self.tail.prev=item
            self.head=item
            item.next=self.tail
        else:
            prev_head=self.head         
            self.head=item
            item.next=prev_head


    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def print_stack(self):
        node=self.head
        while node is not None:
            print(node.value)
            node=node.next

if "__main__"==__name__:
    test_stack=StackHead()
    print (test_stack.size())
    print (test_stack.is_empty())
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(-100)
    test_stack.print_stack()
    test_stack.pop()
    print("##############")
    test_stack.print_stack()
    while test_stack.size() > 0:
        print(f"I've popped the value of {test_stack.pop()}")
        print(f"I've popped the value of {test_stack.pop()}")
    test_stack.print_stack()
    print("##############")
    stack=StackHead()
    for i in range (1,9):
        stack.push(i)
    while stack.size() > 0:
        print (stack.pop())
        print (stack.pop())
    