from src.LinkedList.linked_list_realization import LinkedList, Node

def sum_equal_lists(List1, List2):
    #check if List1 or List2 is Linked list if not return
    if type(List1) is not LinkedList or type(List2) is not LinkedList:
        raise Exception("Types of parameters are not linked list. ")
        return
    #check if some the lists are empty
    if List1.head is None or List2.head is None:
        raise Exception("Lists should not be empty")
        return
    #check if lists are not equal
    if List1.len() != List2.len():
        raise Exception("Lists are not equal. Try again")
        return
    #create new list with sum of every element
    sum_list= LinkedList()
    node1=List1.head
    node2=List2.head    
    while node1 is not None:
        if type(node1.value) is not int or type(node2.value) is not int:
            raise Exception("Lists have not integer values")
            return
        n=Node(node1.value+node2.value)
        sum_list.add_in_tail(n)
        node1=node1.next
        node2=node2.next
    return sum_list
