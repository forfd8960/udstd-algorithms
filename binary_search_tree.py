

class BSTNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root: BSTNode) -> None:
        self.root = root
        self.size = 0
    
    def get(self, key) -> BSTNode:
        if self.root is None:
            return None
        
        node = self.root
        while node != None:
            if node.key == key:
                return node
            
            if node.key > key:
                node = node.left
            else:
                node = node.right
        
        return None
    
    def insert(self, bn: BSTNode) -> None:
        if self.root is None:
            self.root = bn
            return
        
        node = self.root
        while node != None:
            if bn.key > node.key:
                if node.right is None:
                    node.right = bn
                    return
                
                node = node.right
            else:
                if node.left is None:
                    node.left = bn
                    return
                
                node = node.left
    
    def delete(self, key) -> bool:
        return False
