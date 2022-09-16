
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        
    def get_value(self) -> int:
        return self.value
    
    def get_next(self):
        return self.next
  
    def __lt__(self, other) -> bool:
        return self.value < other.value


class LinkedList:
    def __init__(self, head: Node, length: int) -> None:
        self.head = head
        self.tail = self.head
        self.length = length
        
    def get_length(self) -> int:
        return self.length

    def set_head(self, head: Node):
        self.head = head

    def add(self, node: Node) -> None:
        """
        append node to this linked list
        """
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.length = 1
            return
        
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    def __str__(self) -> str:
        nodes = []
        start = self.head
        while start != None:
            nodes.append(start.get_value())
            start = start.get_next()
        
        return '->'.join([str(x) for x in nodes])


def select_sort_linked_list(ll: LinkedList) -> None:
    return None
