class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class OrderedList:
    def __init__(self, asc):
        self.head=None
        self.tail=None
        self.__ascending=asc

    def compare(self,v1,v2):
        if v1<v2:
            return -1
        elif v1==v2:
            return 0
        else:
            return 1
        # -1 if v1 < v2
        # 0 if v1 == v2
        # +1 if v1 > v2


    def add (self, value): #add realization from head to tail
        stop=False
        node_to_add=Node(value)
       
        if self.head is None:
            self.head=node_to_add
            self.tail=node_to_add
        else:
            if self.__ascending:
                 #search from Head
                if self.head is self.tail:                   
                    if self.compare(value,self.head.value) >= 0:
                        self.tail=node_to_add
                        self.head.next=node_to_add
                        self.tail.prev=self.head
                    else:
                        self.head=node_to_add
                        self.tail.prev=self.head
                        self.head.next=self.tail
                else:
                    if self.compare(value, self.head.value) <=0: #add to head
                        old_head=self.head
                        self.head=node_to_add
                        old_head.prev=self.head
                        self.head.next=old_head
                    else:
                        current_from_head=self.head
                        while current_from_head is not None and stop==False:
                            check=self.compare(value, current_from_head.value)
                            if check <= 0:
                                after_node=current_from_head
                                stop=True
                            current_from_head=current_from_head.next
                        
                        if stop:                        
                            before_node=after_node.prev
                            before_node.next=node_to_add
                            after_node.prev=node_to_add
                            node_to_add.next=after_node
                            node_to_add.prev=before_node
                        else:
                            old_tail=self.tail
                            self.tail=node_to_add
                            old_tail.next=node_to_add
                            self.tail.prev=old_tail         
            else:
                if self.head is self.tail:                    
                    if self.compare(value,self.head.value) >= 0: 
                        self.head=node_to_add
                        self.tail.prev=self.head
                        self.head.next=self.tail
                    else:                        
                        self.tail=node_to_add
                        self.head.next=node_to_add
                        self.tail.prev=self.head
                else:
                    if self.compare(value, self.head.value) >= 0: #add to head
                        old_head=self.head
                        self.head=node_to_add
                        old_head.prev=self.head
                        self.head.next=old_head
                    else:
                        current_from_head=self.head
                        while current_from_head is not None and stop==False:
                            check=self.compare(value, current_from_head.value)
                            if check >=0:
                                after_node=current_from_head
                                stop=True
                            current_from_head=current_from_head.next
                        if stop:
                            before_node=after_node.prev
                            before_node.next=node_to_add
                            after_node.prev=node_to_add
                            node_to_add.next=after_node
                            node_to_add.prev=before_node
                        else:
                            old_tail=self.tail
                            self.tail=node_to_add
                            old_tail.next=node_to_add
                            self.tail.prev=old_tail    
    
    def find(self, val):        
        if self.__ascending:
            if self.compare(val,self.head.value)<0:
                return None
            elif self.compare(val,self.tail.value)>0:
                return None
            else:
                current_node=self.head
                while current_node is not None:
                    if self.compare(val,current_node.value) < 0:
                        return None # it is not necessary to search anymore
                    elif self.compare(val,current_node.value) == 0:                                         
                        return current_node
                    current_node=current_node.next
        else:
            if self.compare(val,self.head.value)>0:
                return None
            elif self.compare(val,self.tail.value)<0:
                return None
            else:
                current_node=self.head
                while current_node is not None:
                    if self.compare(val,current_node.value) > 0:
                        return None # it is not necessary to search anymore
                    elif self.compare(val,current_node.value) == 0:                        
                        return current_node
                    current_node=current_node.next
        return None

    def delete(self, val):        
        to_delete=None
        if self.head is None:
            return None
        else:
            if self.__ascending:
                if self.compare(val,self.head.value)<0:
                    return None
                elif self.compare(val,self.head.value)==0:
                    if self.head.next is not None:
                        new_head=self.head.next
                        self.head=new_head
                        new_head.prev=None
                        return
                    else:
                        self.tail=None
                        self.head=None
                        return
                elif self.compare(val,self.tail.value)>0:
                    return None
                elif self.compare(val,self.tail.value)==0:
                    new_tail=self.tail.prev
                    self.tail=new_tail
                    new_tail.next=None
                    return
                else:
                    current_node=self.head
                    while current_node is not None and to_delete is None:
                        if self.compare(val,current_node.value) < 0:
                            return None # it is not necessary to search anymore
                        elif self.compare(val,current_node.value) == 0:                     
                            to_delete=current_node                                             
                        current_node=current_node.next
            else:
                if self.compare(val,self.head.value)>0:
                    return None
                elif self.compare(val,self.head.value)==0:
                    if self.head.next is not None:
                        new_head=self.head.next
                        self.head=new_head
                        new_head.prev=None
                        return
                    else:
                        self.tail=None
                        self.head=None
                        return
                elif self.compare(val,self.tail.value)<0:
                    return None
                elif self.compare(val,self.tail.value)==0:
                    new_tail=self.tail.prev
                    self.tail=new_tail
                    new_tail.next=None
                    return
                else:
                    current_node=self.head
                    while current_node is not None and to_delete is None:
                        if self.compare(val,current_node.value) > 0:
                            return None # it is not necessary to search anymore
                        elif self.compare(val,current_node.value) == 0:                        
                            to_delete=current_node                        
                        current_node=current_node.next
            if to_delete is not None:
                after_node = to_delete.next
                prev_node = to_delete.prev
                after_node.prev=prev_node
                prev_node.next=after_node
            else:
                return None
        

    def clean(self,asc):
        self.__ascending=asc
        self.head=None
        self.tail=None
    
    def len(self):
        n=self.head
        size=0
        while n is not None:
            size+=1
            n=n.next
        return size
    
    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    # def print_all(self):
    #     node=self.head
    #     if self.__ascending:
    #         print("The list is ascending")
    #     else:
    #         print("The list is descending")
    #     print(f'The head is {self.head.value}')
    #     print(f'The tail is {self.tail.value}')
    #     while node is not None:
    #         print(node.value)
    #         node=node.next
            

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super().__init__(asc)

    def compare(self, v1, v2):
        v1=v1.strip()
        v2=v2.strip()
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        elif v1==v2:
            return 0

# if __name__ == "__main__":
#     test_value=[123,1000,-432,1,0,12345,0,123,-321]
#     o_list_desc=OrderedList(False)
#     o_list_asc=OrderedList(True)
#     for item in test_value:
#         o_list_desc.add(item)
#         o_list_asc.add(item)
#     o_list_desc.print_all()
#     o_list_asc.print_all()

    
    

    