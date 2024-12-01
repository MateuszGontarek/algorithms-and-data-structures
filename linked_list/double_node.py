class DoubleNode:
    __slots__ = "value", "next", "prev"

    def __init__(self, value: int, prev = None, next = None) -> None:
        self.value = value
        self.prev: DoubleNode = prev
        self.next: DoubleNode = next

    def __str__(self) -> str:
        return str(self.value)