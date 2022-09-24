
# Impl with LRU Cache with linked list
from ..linked_list import LinkedList

class LRUCache:
    def __init__(self, max_size: int) -> None:
        self.ll = LinkedList(None, 0)
        self.size = 0
        self.max_size = max_size
    
    def get(self, key: str):
        start = self.ll.head
        target_node = None
        while start != None:
            if key == start.get_value():
                target_node = start
                break
            
            start = start.get_next()
            
        if target_node is None:
            return -1, False
            
        return -1, False
     
    def set(self, key: str, value: int) -> None:
         return None
