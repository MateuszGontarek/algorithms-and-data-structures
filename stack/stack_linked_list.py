from node import Node

class StackLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0        
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not len(self)
    
    def push(self, value: int) -> None:
        node = Node(value)

        if self.is_empty():
            self.head = node
            return
        
        node.next = self.head
        self.head = node
        self.size += 1

    def top(self) -> int|None:
        if self.is_empty():
            print("Stack is empty")
            return

        return self.head.value

    def pop(self) -> int|None:
        if self.is_empty():
            print("Stack is empty")
            return
        
        value = self.head.value

        self.head = self.head.next
        self.size -= 1

        return value
        