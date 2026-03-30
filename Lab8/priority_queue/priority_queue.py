from __future__ import annotations

from typing import Iterator, Generic, TypeVar, Optional
#from rich.protocol import rich_cast
from fifo_queue import QueueUnderflowError, QueueOverflowError

A = TypeVar("A")

class PriorityQueue(Generic[A]):
    """A prioritized first-in first-out (FIFO) collection of elements."""

    def __init__(self, elements: Optional[list[A]] = None, maxsize: Optional[int] = None):
        """
        Create a queue
        :param elements:
        :param capacity:
        """
        self._elements: list[A] = [] if elements is None else elements.copy()
        self._cursor: int = 0
        self._capacity: Optional[int] = maxsize

    def put(self, element: A):
        """
        Add an element on the rear of the queue. Precondition: queue not full.
        :param element: The element to add to the queue.
        """
        if self.full():
            raise QueueOverflowError()

        # TODO: add your put code here!
        self._elements.append(element)

    def get(self, block=True) -> A:
        """
        Remove the front element of the queue. Precondition: queue not empty.
        :return: The element removed from the queue.
        """
        if self.empty():
            raise QueueUnderflowError()

        # TODO: add your get code here!
        # lowest = self._elements[0]
        # for e in _elements:
        #     if e < lowest:
        #           lowest = e
        # _elements.remove(e)
        # return lowest

        


    @property
    def not_empty(self):
        return not self.empty()

    # These next two propertie are needed to match the API of the Priority queue
    @property
    def queue(self) -> PriorityQueue:
        return self

    @property
    def maxsize(self) -> int:
        return self._capacity

    def empty(self) -> bool:
        """Determine if the queue is empty."""
        return len(self._elements) == 0

    def full(self) -> bool:
        """Determine if the queue is full."""
        if self._capacity is not None:
            return len(self._elements) == self._capacity
        else:
            return False

    def __iter__(self) -> Iterator[int]:
        self._cursor = -1
        return self

    def __next__(self) -> A:
        if self._cursor >= len(self._elements) - 1:
            raise StopIteration
        self._cursor += 1
        return self._elements[self._cursor]

    def __str__(self):
        return f"FRONT --> {self._elements} <-- REAR"

    def __repr__(self):
        if self._capacity is None:
            return f"PriorityQueue({repr(self._elements)})"
        else:
            return f"PriorityQueue({repr(self._elements)}, {self._capacity})"
