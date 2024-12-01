class Deque:
    def __init__(self) -> None:
        self.data: list[int] = []

    def __len__(self) -> int:
        return len(self.data)
    
    def is_empty(self) -> bool:
        return not len(self)
    
    def add_first(self, value: int) -> None:
        self.data.insert(0, value)
    
    def add_last(self, value: int) -> None:
        self.data.append(value)
    
    def first(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return

        return self.data[0]

    def last(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return

        return self.data[-1]
    
    def remove_first(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return
        
        return self.data.pop(0)
    
    def remove_last(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return
        
        return self.data.pop()
       