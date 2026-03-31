from typing import TypeVar, Optional
T = TypeVar("T")
class Link[T]:
    """Stores a single element in a link 'chain'."""
    def __init__(self, element:  T):
        self.element: T = element
        self.next: Optional[Link[T]] = None
class linked_list[T]:
    """A link chain implementation of a list."""
    def __init__(self):
        self.head: Optional[Link[T]] = None
        self.tail: Optional[Link[T]] = None
        self.tracker = self.head
    # ITER METHOD ----------------------------------------------------------
    def __iter__(self):
        self.tracker = self.head
        return self
    # NEXT METHOD ----------------------------------------------------------
    def __next__(self):
        if self.tracker is None:
            raise StopIteration
        result = self.tracker.element
        self.tracker = self.tracker.next
        return result


    def append(self, x: T):
        new_link = Link(x)
        if self.head is None: # If True head hasn't been set yet
            self.head = new_link # First node is both head and tail
        else:
            self.tail.next = new_link # Move new node to end
        self.tail = new_link # tail always moves to the newest node
    def insert(self, index: int, x: T):
        if index > len(self):
            raise IndexError("Out of range")
        new_link = Link(x)
        if index == 0:
            new_link.next = self.head
            self.head = new_link
            if self.tail is None:
                self.tail = new_link
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_link.next = current.next
        current.next = new_link
        if new_link.next is None:
            self.tail = new_link
    def __len__(self) -> int:
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
# TESTING ITERATION --------------------------------------------------------------------
my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
for i in my_list:
    print(i)
for i in my_list:
    print(i)