class Queue:
    def __init__(self) -> None:
        self.data: list[int] = []

    def __len__(self) -> int:
        return len(self.data)
    
    def is_empty(self) -> bool:
        return not len(self)
    
    def enqueue(self, value: int) -> None:
        self.data.append(value)
    
    def first(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return

        return self.data[0]

    def dequeue(self) -> int|None:
        if self.is_empty():
            print("Queue is empty")
            return
        
        return self.data.pop(0)
        