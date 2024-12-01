from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not self.size
    
    def add_last(self, value: int) -> None:
        node = Node(value)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node
        self.size += 1
    
    def remove_last(self) -> int:
        if self.is_empty():
            print("List is empty")
            return

        node = self.head
        i = 1
        
        while i < self.size - 1:
            node = node.next
            i += 1

        self.tail = node
        node = node.next
        self.size -= 1
        self.tail.next = None

        return node.value
    
    def add_at_beggining(self, value: int) -> None:
        node = Node(value)

        if self.is_empty():
            self.head = node
            self.tail = node
            return
        
        node.next = self.head
        self.head = node
        self.size += 1

    def add(self, value: int, position: int) -> None:
        node = Node(value)
        p = self.head
        
        for _ in range(position - 2):
            p = p.next      
        
        node.next = p.next
        p.next = node
        self.size += 1

    def remove(self, position: int) -> int:
        node = self.head
        
        for _ in range(position - 2):
            node = node.next
        
        value = node.next.value
        node.next = node.next.next
        self.size -= 1

        return value

    def display(self) -> None: 
        node = self.head
        
        while node:
            print(node, end="")
            if node.next: 
                print(" -> ", end="")
            
            node = node.next

    def search(self, key: int) -> int:
        node = self.head
        index = 0 
        
        while node:
            if node.value == key:
                return index

            index += 1
            node = node.next
        return -1