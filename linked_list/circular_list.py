from node import Node

class CircularList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size = 0
    
    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not self.size

    def add(self, value: int, position: int) -> None:
        node = Node(value)

        p = self.head
        
        for _ in range(position - 2):
            p = p.next

        node.next = p.next
        p.next = node

    def add_first(self, value: int) -> None: 
        node = Node(value)

        if self.is_empty():
            node.next = node
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.head = node
        
        self.size += 1
    
    def add_last(self, value) -> None:
        node = Node(value)

        if self.is_empty():
            node.next = node
            self.head = node
        else:
            node.next = self.tail.next
            self.tail.next = node
        
        self.tail = node
        self.size += 1

    def remove_first(self) -> int:
        if self.is_empty():
            print("List is empty")
            return
        
        value = self.head.value
        
        self.tail.next = self.head.next
        self.head = self.head.next

        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail = None
        return value
    
    def remove_last(self) -> int:
        if self.is_empty():
            print("List is empty")
            return
        
        node = self.head

        for _ in range(1, self.size - 1):
            node = node.next

        value = node.next.value
        node.next = self.head
        
        self.size -= 1
        self.tail = node

        return value

    def remove(self, position: int) -> int:
        if self.is_empty():
            print("List is empty")
            return
        
        node = self.head

        for _ in range(1, position - 2):
            node = node.next

        value = node.next.value
        node.next = node.next.next

        self.size -= 1
        return value

    def display(self):
        node = self.head
        i = 0
        
        while i < self.size:
            print(node, end="-->")
            node = node.next
            i += 1
        
        print()

            