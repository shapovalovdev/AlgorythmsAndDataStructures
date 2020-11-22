
from src.Stack.stack_linked_list import Stack

def calculate_postfix(expression):
    S=Stack()
    if not expression:
        raise Exception("The string is empty")
    for item in expression:
        if item.isdigit():
            S.push(int(item))
        elif item == "+":
            val1=S.pop()
            val2=S.pop()
            S.push(val1+val2)
        elif item=="*":
            val1=S.pop()
            val2=S.pop()
            S.push(val1*val2)
        elif item=="-":
            val1=S.pop()
            val2=S.pop()
            S.push(val1-val2)
        elif item=="/":
            val1=S.pop()
            val2=S.pop()
            S.push(val1/val2)

        elif item=="=":
            return S.pop()
    return S.pop()

if __name__ == "__main__":
    print(calculate_postfix("8 2 + 5 * 9 +"))
    
