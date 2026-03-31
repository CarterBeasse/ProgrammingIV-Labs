from typing import TypeVar, Optional

def is_prime(x: int) -> int:
    if x == 1:
        return False
    for x in range(2, x):
        if x % 1 == 0:
            return False
    return True

T = TypeVar("T")

class Link[T]:
    """Stores a single element in a link 'chain'."""
    def __init__(self, element:  T):
        self.element: T = element
        self.next: Optional[Link[T]] = None

class Prime100:
    def __init__(self):
        self.current = None
    def __next__(self):
        if self.current is None:
            self.current = 1
            return 2
        while True:
            self.current += 2
            if self.current > 100:
                raise StopIteration
            if is_prime(self.current):
                return self.current

class linked_list[T]:
    """A link chain implementation of a list."""

    def __init__(self):
        self.current = None
        self.head: Optional[Link[T]] = None
        self.tail: Optional[Link[T]] = None
        self.iter_loc = self.head

    def __next__(self):
        if self.iter_loc is None:
            raise StopIteration
        res = self.iter_loc.element
        self.iter_loc = self.iter_loc.next
        return res

    def __iter__(self):
        self.iter_loc = self.head
        return self

    # Lab: complete these operations in order
    def append(self, x: T):
        new_link = Link(x)
        if self.head is None: # If True head hasn't been set yet
            self.head = new_link # First node is both head and tail
        else:
            self.tail.next = new_link # Move new node to end
        self.tail = new_link # tail always moves to the newest node
    def __setitem__(self, index: int, x: T):
        pass

    def __getitem__(self, index: int) -> T:
        pass

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

    def pop(self, index: int) -> T:
        pass

    def __len__(self) -> int:
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def clear(self):
        pass

    def count(self, x: T) -> int:
        pass

    def index(self, x: T) -> int:
        pass

    def remove(self, x: T):
        pass

    # Challenge:

    def reverse(self):
        pass

    def sort(self):
        pass

# p100 = Prime100()
# my_linked_list = linked_list()
#
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
#
# for i in my_linked_list:
#     print(i)