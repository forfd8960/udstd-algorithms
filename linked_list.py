
from asyncio import proactor_events


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        
    def get_value(self) -> int:
        return self.value
    
    def get_next(self):
        return self.next
    
    def __str__(self) -> str:
        return f'{self.value}'
  
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
        
    def get_head(self):
        return self.head

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
        
    def add_nodes(self, nodes: list[Node]) -> None:
        for node in nodes:
            self.add(node)
            
    def get_mid(self) -> Node:
        """
        In [1]: from linked_list import LinkedList, Node
        In [2]: ll = LinkedList(None, 0)

        In [3]: ll.add_nodes([Node(3, None), Node(6, None),Node(9, None),Node(12, None), Node(15, None)])

        In [4]: n = ll.get_mid()

        In [5]: n.value
        Out[5]: 9

        In [6]: ll1 = LinkedList(None, 0)

        In [10]: ll1.add_nodes([Node(1, None), Node(2, None)])

        In [11]: mid = ll1.get_mid()

        In [12]: mid.value
        Out[12]: 2

        In [13]: ll1.delete_nth_node_from_tail(1)
        Out[13]: <linked_list.Node at 0x1053af520>

        In [14]: print(ll1)
        1

        In [15]: mid = ll1.get_mid()

        In [16]: mid.value
        Out[16]: 1
        """
        start = self.head
        i = 0
        while i < self.length // 2:
            start = start.next
            i += 1

        return start

    def delete_nth_node_from_tail(self, n) -> Node:
        """
        In [1]: from linked_list import LinkedList, Node

        In [2]: ll = LinkedList(None, 0)

        In [3]: ll.add_nodes([Node(3, None), Node(6, None),Node(9, None),Node(12, None), Node(15, None)])

        In [4]: print(ll)
        3->6->9->12->15

        In [5]: ll.delete_nth_node_from_tail(1)
        2 None 3
        3 3 6
        4 6 9
        5 9 12
        Out[5]: <linked_list.Node at 0x10351e710>

        In [6]: print(ll)
        3->6->9->12

        In [7]: ll.length
        Out[7]: 4

        In [8]: ll.delete_nth_node_from_tail(4)
        Out[8]: <linked_list.Node at 0x105be2fb0>

        In [9]: print(ll)
        6->9->12

        In [10]: ll.head.value
        Out[10]: 6

        In [11]: ll.tail.value
        Out[11]: 12
        """
        if n < 1 or n > self.length:
            return None
        
        if n == self.length:
            rt = Node(self.head.get_value(), None)
            self.head = self.head.next
            self.length -= 1
            return rt

        node = self.head
        prev = None
        i, end = 2, self.length - n + 1
        while i <= end:
            prev = node
            node = node.next
            i += 1

        if n == 1:
            self.tail =  prev

        prev.next = node.next
        self.length -= 1
        return node

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


"""
In [1]: from linked_list import LinkedList, Node, merge_sorted_linked_list

In [2]: ll = LinkedList(None, 0)

In [4]: ll.add_nodes([Node(1, None), Node(2, None),Node(3, None),Node(4, None)])

In [5]: print(ll)
1->2->3->4

In [6]: ll1 = LinkedList(None, 0)

In [7]: ll1.add_nodes([Node(3, None), Node(6, None),Node(9, None),Node(12, None), Node(15, None)])

In [8]: print(ll1)
3->6->9->12->15

In [9]: new_ll = merge_sorted_linked_list(ll, ll1)

In [10]: print(new_ll)
1->2->3->3->4->6->9->12->15
"""
def merge_sorted_linked_list(l1: LinkedList, l2: LinkedList) -> LinkedList:
    head1 = l1.get_head()
    head2 = l2.get_head()
    new_ll = LinkedList(None, 0)
    
    while head1 != None and head2 != None:
        if head1.get_value() <= head2.get_value():
            new_ll.add(head1)
            head1 = head1.get_next()
        else:
            new_ll.add(head2)
            head2 = head2.get_next()
            
    if head1 != None:
        while head1 != None:
            new_ll.add(head1)
            head1 = head1.get_next()
    if head2 != None:
        while head2 != None:
            new_ll.add(head2)
            head2 = head2.get_next()

    return new_ll
