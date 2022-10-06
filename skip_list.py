# python3


class SkipListNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.forward = []


class SkipList:
    def __init__(self, max_level: int) -> None:
        self.head = None
        self.max_level = max_level
        self.level = 0
    
    def add(self, key, value) -> None:
        if self.head is None:
            self.head = SkipListNode(key, value)
            self.head.forward = [None]
            self.level = 0
        else:
            return
            
    def delete(self, key) -> None:
        return None

    def search(self, key) -> SkipListNode:
        level = self.level
        n = self.head
        while level >= 0:
            if n.key == key:
                break
            
            if n.forward[level] is None:
                level -= 1
                continue

            next = n.forward[level]
            if next.key > key:
                level -= 1
                continue
            
            while next != None and key >= next.key:
                n = next
                next = next.forward[level]

            i -= 1

        if n.key != key:
            return None
        
        return n 
    
    def range_values(self, min, max) -> None:
        return None
