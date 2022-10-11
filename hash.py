
# default cap of hash buckets
DEFAULT_CAP = 10

from linked_list import LinkedList, Node


class KV:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        
    def __eq__(self, other) -> bool:
        return self.key == other.key
    
    def __str__(self) -> str:
        return f'[{self.key}: {self.value}]'


class Hash:
    def __init__(self, load_factor: float, cap: int) -> None:
        if cap <= 0:
            cap  = DEFAULT_CAP

        self.cap = cap
        self.bucket_size = 0
        self.buckets = [None for _ in range(0, cap)]
        self.load_factor = load_factor

    def put(self, key, value) -> bool:
        idx = hash(key) % len(self.buckets)
        bucket = self.buckets[idx]
        
        kv = KV(key, value)
        if bucket is None:
            bucket = LinkedList(Node(kv, None), 1)
            self.buckets[idx] = bucket
            self.bucket_size += 1
            self.grow()
            return True
        
        found_node = bucket.find(kv)
        if found_node is None:
            bucket.add(Node(kv, None))
            return True
        
        found_node.update_value(kv)
        return True
    
    def grow(self):
        if self.bucket_size / len(self.buckets) < self.load_factor:
            return
        
        print("grow hash to double size")

        new_buckets = [None for _ in range(0, len(self.buckets)*2)]
        new_length = len(new_buckets)
        bucket_size = 0
        for bucket in self.buckets:
            if bucket is None:
                continue
            
            nodes = bucket.iterate()
            if len(nodes) == 0:
                continue
            
            print(f"move bucket nodes: {bucket} to new buckets")
            
            for node in nodes:
                kv = node.get_value()
                idx = hash(kv.key) % new_length
                
                bucket = new_buckets[idx]
                if bucket is None:
                    new_buckets[idx] = LinkedList(node, 1)
                    bucket_size += 1
                else:
                    bucket.add(node)

        self.buckets = new_buckets
        self.bucket_size = bucket_size

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
        if bucket is None:
            return False

        kv = KV(key, None)
        ok = bucket.remove(kv)
        if ok and bucket.is_empty():
            self.bucket_size -= 1

        return ok
