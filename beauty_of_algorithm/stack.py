
class Stack:
    """
    When a data structure can pop and push on one end, and need to be first in, later out.
    then this data strucutre is Stack
    """
    
    def __init__(self) -> None:
        self.elements = []
        
    def push(self, e) -> None:
        self.elements.append(e)
        
    def is_empty(self) -> bool:
        return len(self.elements) == 0
    
    def pop(self):
        if len(self.elements) == 0:
            return None
        
        last = len(self.elements) - 1
        e = self.elements[last]
        self.elements = self.elements[:last]
        return e


def parenthesis_match(exp: str) -> bool:
    """
    Check if the {}, [], () is matching in the exp
    """
    
    left = ["{", "[", "("]
    right = ["}", "]", ")"]
    stack = Stack()
    
    for c in exp:
        if c in left:
            stack.push(c)

        if c in right:
            if stack.is_empty():
                return False
            
            e = stack.pop()
            if not is_match(e, c):
                return False

    return stack.is_empty()


def is_match(left, right):
    if left == "{": return right == "}"
    if left == "[": return right == "]"
    if left == "(": return right == ")"
    
    return False
