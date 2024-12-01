from double_node import DoubleNode

class LinkedList:
    def __init__(self) -> None:
        self.head: DoubleNode = None
        self.tail: DoubleNode = None
        self.size = 0

    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return not self.size
    
    def add_last(self, value: int) -> None:
        node = DoubleNode(value)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1
    
    def remove_first(self) -> int:
        if self.is_empty():
            print("List is empty")
            return
        
        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

        if self.is_empty():
            self.tail = None
        
        return value
    
    def remove_last(self) -> int:
        if self.is_empty():
            print("List is empty")
            return

        value = self.tail.value
        
        self.tail = self.tail.prev
        self.size -= 1
        self.tail.next = None

        return value
    
    def add_at_beggining(self, value: int) -> None:
        node = DoubleNode(value)

        if self.is_empty():
            self.head = node
            self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

        self.size += 1

    def add(self, value: int, position: int) -> None:
        node = DoubleNode(value)
        p = self.head
        
        for _ in range(position - 2):
            p = p.next      
        
        node.next = p.next
        p.next.prev = node
        p.next = node
        node.prev = node

        self.size += 1

    def remove(self, position: int) -> int:
        node = self.head
        
        for _ in range(position - 2):
            node = node.next
        
        value = node.next.value
        node.next.prev = node 
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
    
    def display_rev(self) -> None: 
        node = self.tail
        
        while node:
            print(node, end="")
            if node.prev: 
                print(" -> ", end="")
            
            node = node.prev
    
    def search(self, key: int) -> int:
        node = self.head
        index = 0 
        
        while node:
            if node.value == key:
                return index

            index += 1
            node = node.next
        return -1