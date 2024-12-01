from node import Node

class DequeLinkedList:
    def __init__(self) -> None:
        self.front: Node = None
        self.rear: Node = None
        self.size: int = 0        
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not len(self)
    
    def add_first(self, value: int) -> None:
        node = Node(value)

        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            node.next = self.front
            self.front = node

        self.size += 1
    
    def add_last(self, value: int) -> None:
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

    def last(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return

        return self.rear.value
    
    def remove_first(self) -> int|None:
        if self.is_empty():
            print("List is empty")
            return
        
        value = self.front.value

        self.front = self.front.next

        self.size -= 1

        if self.is_empty():
            self.rear = None
        
        return value
    
    def remove_last(self) -> int|None:
        if self.is_empty():
            print("List is empty")
            return
        
        value = self.rear.value

        node = self.front
        for _ in range(self.size - 2):
            node = node.next
        
        self.rear = node
        self.rear.next = None

        self.size -= 1

        if self.is_empty():
            self.rear = None
        
        return value

    def search(self, key: int) -> int:
        node = self.front   
        if node.value == key: return 0  
        
        index = 1

        while node := node.next:
            if node.value == key:
                return index

            index += 1

        return -1