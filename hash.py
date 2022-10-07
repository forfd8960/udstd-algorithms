
# default cap of hash buckets
DEFAULT_CAP = 10

from linked_list import LinkedList, Node


class KV:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        
    def __eq__(self, other) -> bool:
        return self.key == other.key


class Hash:
    def __init__(self, load_factor: float, cap: int) -> None:
        if cap <= 0:
            cap  = DEFAULT_CAP

        self.cap = cap
        self.buckets = [None for _ in range(0, cap)]
        self.load_factor = load_factor

    def put(self, key, value) -> bool:
        idx = hash(key) % len(self.buckets)
        bucket = self.buckets[idx]
        
        kv = KV(key, value)
        if bucket is None:
            bucket = LinkedList(Node(kv, None), 1)
            self.buckets[idx] = bucket
            return True
        
        found_node = bucket.find(kv)
        if found_node is None:
            bucket.add(Node(kv, None))
            return True
        
        found_node.update_value(kv)
        return True

    def get(self, key) -> tuple:
        idx = hash(key) % len(self.buckets)
        bucket = self.buckets[idx]
        
        kv = KV(key, None)
        found_node = bucket.find(kv)
        if found_node is None:
            return None, False
        
        return found_node.value, True
    
    def remove(self, key) -> bool:
        idx = hash(key) % len(self.buckets)
        bucket = self.buckets[idx]
        
        kv = KV(key, None)
        return bucket.remove(kv)
