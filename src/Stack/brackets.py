from src.Stack.stack_linked_list  import Stack

def is_balanced(brackets):
    brackets=brackets.strip()
    if brackets=='':
        raise Exception("The string is empty")
    if '(' not in brackets  and ')' not in  brackets:
        raise Exception("This string without brackets")
    stack=Stack()
    for bracket in brackets:
        if bracket==')' and stack.is_empty():
            print ("The string is started with closed bracket and it is  not balanced")
            return False
        elif bracket=='(':
            stack.push(bracket)
        elif bracket==')':
            stack.pop()
        else:
            raise Exception("This string has something else but brackets")
    if stack.is_empty():
        print ("The string is balanced")
        return True
    else:
        print ("The string is not balanced")
        return False
    
        
if __name__=="__main__":
    is_balanced('((')
    is_balanced('()')