class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head=item
        else:
            self.tail.next = item
        
        self.tail = item
    
    def print_all_nodes(self):
        node=self.head
        while node is not None:
            #print(node.value)
            node = node.next
    
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node=node.next
        return None

    def delete(self,val, all=False):
        node=self.head
        node_previous=self.head           
        while node is not None:
            if node.value == val:
                 
                if node is self.head and node is self.tail:
                    self.head=None
                    self.tail=None
                if node is self.head:
                    self.head=node.next
                    
                node_previous.next=node.next
                if node is self.tail:
                    self.tail=node_previous

                if all==False:
                    break
                
            else:
                node_previous=node
            node=node.next
    def clean(self):
        self.head = None
        self.tail = None
    
    def find_all(self, val):
        finding=[]
        node=self.head
        while node is not None:
            if node.value == val:
                finding.append(node)
            node=node.next        
        return finding
    def len(self):
        node = self.head
        length=0
        while node is not None:
            length+=1
            node = node.next
        return length
    
    def insert(self, afterNode, newNode):
        node=self.head
        if node is None and afterNode is None: #case of empty list
            self.head=newNode
            self.tail=newNode
        while node is not None:
            if node is afterNode:
                if node is self.tail:
                    self.tail=newNode                
                newNode.next=node.next
                node.next=newNode
                break                
            node=node.next
