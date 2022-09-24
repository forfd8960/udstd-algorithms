
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
        
    def iterate(self) -> list[Node]:
        nodes = []
        start = self.head
        while start != None:
            nodes.append(start)
            start = start.get_next()
            
        return nodes
    
    def reverse(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            return
        
        tmp = self.head
        tmp_next = self.head.next
        self.tail = self.head
        
        while tmp_next != None:
            temp = tmp_next.next
            tmp_next.next = tmp
            tmp, tmp_next = tmp_next, temp
        
        self.head = tmp
        self.tail.next = None

    def __str__(self) -> str:
        return '->'.join([str(x.get_value()) for x in self.iterate()])


def select_sort_linked_list(ll: LinkedList) -> None:
    return None
