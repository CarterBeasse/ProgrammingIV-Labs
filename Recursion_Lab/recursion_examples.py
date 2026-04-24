# For these exercises create both the public and helper functions.
# The user/developper should call the public function while the helper does the actual recursive task

# Exercise: implement a `is_palindrome` method recursively
"""
A *palindrome* is a word (or sentence) whose spelling is the same when
read forwards or backwards. Examples of palindromes: "racecar", "taco
cat", "tattarrattat".
"""

def is_palindrome(word: str, left: int, right: int):
    pass

# Exercise: Implement a recursive filter
"""
Write a function that recursively filters a list, returning a new list with all the entries that satisfy the filter's condition.
Can you do this with both tail and non-tail recursion?
"""

def sample_filter(x: float):
    # A simple filter that checks if a grade is passing
    return x >= 60

def filter_list(vals: list[float]) -> list[float]:
    pass


#TODO: Implement a binary search recursively.

def bin_Search(src, target):
    pass
def bin_Search_h(src,left,right,target):
    pass


# Exercise: Implement a DFS recursively

# Adapted from the search algorithm assignment.
class DFSRecursive(Search):

    def solve(self) -> Iterable[Direction]:
        super().solve()
        self.dfs_visit(self.terrain.start, set())

    def dfs_visit(self, current: Position, visited: set[Position]) -> bool:
        pass

# Exercise: Merge Sort:
"""
MergeSort is a recursive sorting algorithm that is efficient. It's especially useful when sorting data stored in structures that have slow random access, ex: files, chains, etc…

Before we tackle the sort algorithm, let's implement the method merge. It does most of the work in the algorithm!

Merge
A merge takes two sorted list sublists and combines them into a third sublist in such a way that the elements are sorted.

The setup is based on how we plan on calling merge(..) from within the sort:

The two sublists are next to each other in the list src[left..mid] and src[mid+1..right]. We call them contiguous.
Precondition 1: left < mid and mid + 1 < right.
Precondition 2: sublist src[left..mid] and src[mid+1..right] are sorted ascending.
The merged elements are put into dst.
"""
#Note that this merge function is not recursive, but it is used in the recursive mergesort
def merge(src: list[A], low: int, mid: int, high: int, dst: list[Optional[A]]):
    """Merge src[low:mid] with src[mid+1:high] into dst[low:high].
       Assumes that src[low:mid] and src[mid+1:high] are individually sorted when this is called"""
       pass