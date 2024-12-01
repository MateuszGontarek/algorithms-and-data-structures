class Stack:
    def __init__(self) -> None:
        self.data: list[int] = []
        
    def __len__(self) -> int:
        return len(self.data)
    
    def is_empty(self) -> bool:
        return not len(self)
    
    def push(self, value: int) -> None:
        self.data.append(value)
    
    def top(self) -> int|None:
        if self.is_empty():
            print("Stack is empty")
            return

        return self.data[-1]

    def pop(self) -> int|None:
        if self.is_empty():
            print("Stack is empty")
            return
        
        return self.data.pop()
        