from node import Node

class QueueLinkedList:
    def __init__(self) -> None:
        self.front: Node = None
        self.rear: Node = None
        self.size: int = 0        
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not len(self)
    
    def enqueue(self, value: int) -> None:
        node = Node(value)

        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        self.size += 1

    def first(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return

        return self.front.value

    def dequeue(self) -> int|None:
        if self.is_empty():
            print("List is empty")
            return
        
        value = self.front.value

        self.front = self.front.next

        self.size -= 1

        if self.is_empty():
            self.rear = None
        
        return value
        