class Node:
    __slots__ = "value", "next"

    def __init__(self, value: int, next = None) -> None:
        self.value = value
        self.next: Node = next

    def __str__(self) -> str:
        return str(self.value)