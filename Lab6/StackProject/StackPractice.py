class StackOverflowException(Exception):
 """Stack overflow error"""
class StackUnderflowException(Exception):
 """Stack underflow error"""

class StackClass:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.stack: list[str] = []

    def push(self, element: str):
        stack_length = len(self.stack)

        if stack_length < self.capacity:
            self.stack.append(element)
        else:
            pass

    def pop(self) -> str:
        stack_length = len(self.stack)

        if stack_length > 0:
            removed_item = self.stack.pop()
            return removed_item
        else:
            return "Error!"

    def top(self)-> str:
        stack_length = len(self.stack)

        if stack_length > 0:
            return self.stack[-1]
        else:
            return "Error!"

    def empty(self) -> bool:
        stack_length = len(self.stack)

        if stack_length > 0:
            return False
        else:
            return True

    def full(self) -> bool:
        stack_length = len(self.stack)

        if stack_length >= self.capacity:
            return True
        else:
            return False

    def get_capacity(self) -> int:
        return self.capacity






