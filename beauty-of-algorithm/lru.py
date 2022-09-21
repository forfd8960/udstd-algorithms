
# Impl with LRU Cache with linked list
from ..linked_list import LinkedList

class LRUCache:
    def __init__(self, max_size: int) -> None:
        self.ll = LinkedList(None, 0)
        self.size = 0
        self.max_size = max_size
    
    def get(self, key: str):
         return -1, False
     
    def set(self, key: str, value: int) -> None:
         return None
