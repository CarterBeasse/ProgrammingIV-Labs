from __future__ import annotations

from asyncio import new_event_loop
from typing import TypeVar, Optional

T = TypeVar("T")

class Link[T]:
    """Stores a single element in a link 'chain'."""
    def __init__(self, element:  T):
        self.element: T = element
        self.next: Optional[Link[T]] = None


class linked_stack[T]:
    """A link chain implementation of a stack."""
    def __init__(self):
        self.head: Optional[Link[T]] = None
        
    def push(self, x: T): # Head -> [A] -> [B]
        new_link = Link(x) #Create new_link [X]
        new_link.next  = self.head #Connect new_link to old head | [X] -> [A]
        self.head = new_link #Update head to [X] | Head -> [X] -> [A] -> [B]

    def pop(self) -> T:
        current_head = self.head #Save the current head link | current_head -> [A] -> [B] -> None
        new_head = self.head.next #Find the new link(will become new head) | new_head -> [B] -> None
        self.head = new_head #Move the head to the next link | current_head -> [A] & new_head -> [B] -> None
        return current_head.element #Return the value that was stored in the old head | Return A

    def peek(self) -> T:  # a.k.a. top()
        return self.head.element
    
    def is_empty(self) -> bool:
        return self.head is None


    def is_full(self) -> bool:
        return False #Linked chain always grows so it's never full


class linked_queue[T]:
    """A link chain implementation of a queue."""

    def __init__(self):
        self.head: Optional[Link[T]] = None
        self.tail: Optional[Link[T]] = None
        
    def put(self, x: T):
        new_link = Link(x) #Make a new Link
        if self.is_empty(): #If queue is empty set the new link as head
            self.head = new_link
        else:
            self.tail.next = new_link
        self.tail = new_link

    def get(self) -> T:
        if self.is_empty():
            return "Can't get when queue is empty"
        current_head = self.head
        new_head = self.head.next
        self.head = new_head
        return current_head.element

    def peek(self) -> T:  # a.k.a. front()
        return self.head.element

    def is_empty(self) -> bool:
        return self.head is None

    def is_full(self) -> bool:
        return False

    
class linked_list[T]:
    """A link chain implementation of a list."""

    def __init__(self):
        self.head: Optional[Link[T]] = None
        self.tail: Optional[Link[T]] = None
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

    def copy(self) -> linked_list[T]:
        pass

    # Challenge:

    def reverse(self):
        pass

    def sort(self):
        pass

