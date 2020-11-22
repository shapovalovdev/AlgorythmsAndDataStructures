from src.Deque.deque_scratch import Deque

def is_palindrome(string_to_check):
    string_to_check=string_to_check.strip()
    if not string_to_check:
        raise Exception("The string is empty")
    
    deq=Deque()
    for el in string_to_check:
        deq.addTail(el)
    front=deq.removeFront()
    end=deq.removeTail()
    while front == end and front is not None and end is not None:
        if deq.size() == 1:
            return True
        front=deq.removeFront()
        end=deq.removeTail()
    if deq.size() == 0:
        return True
    else:
        return False
    
        
