
class Queue:
    """
    In [1]: from beauty_of_algorithm.queue import Queue
    In [2]: queue = Queue(10)
    In [3]: for i in range(1, 11):
    ...:     r = queue.enqueue(i)
    ...:     print(f"enqueue result: {i}")
    ...: 
    enqueue result: 1
    enqueue result: 2
    enqueue result: 3
    enqueue result: 4
    enqueue result: 5
    enqueue result: 6
    enqueue result: 7
    enqueue result: 8
    enqueue result: 9
    enqueue result: 10

    In [4]: queue.head
    Out[4]: 0

    In [5]: queue.tail
    Out[5]: 10

    In [6]: r = queue.enqueue(11)

    In [7]: r
    Out[7]: False

    In [8]: r = queue.dequeue()

    In [9]: r
    Out[9]: 1

    In [10]: r = queue.dequeue()

    In [11]: r
    Out[11]: 2

    In [12]: queue.tail
    Out[12]: 10

    In [13]: queue.head
    Out[13]: 2

    In [14]: queue.cap
    Out[14]: 10

    In [15]: queue.elements
    Out[15]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.elements = []
        self.head = 0
        self.tail = 0
        
        i = 1
        while i <= cap:
            self.elements.append(None)
            i += 1
            
    def enqueue(self, e) -> bool:
        # if there is no space for new element, then we can move all rest elements to head
        if self.tail == self.cap:
            if self.head == 0: # whole queue is full
                return False
            
            # Move all rest elements start from head
            i = self.head
            while i < self.tail:
                self.elements[i - self.head] = self.elements[i]
                i += 1
            
            self.tail -= self.head
            self.head = 0

        self.elements[self.tail] = e
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        
        e = self.elements[self.head]
        self.head += 1
        return e

