from typing import Any

class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in last-in, first-out order. When removing an item from the stack,
    the most recently-added item is the one that is removed.
    """

    def __init__(self):
        """Initializes a new, empty stack"""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('hello')
        >>> s.is_empty()
        False
        """
        return len(self._items) == 0

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.
        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        return self._items.pop()

    def peek(self) -> Any:
        """Return the element at the top of this stack.
        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.peek()
        'goodbye'
        >>> s.peek()
        'goodbye'
        """
        return self._items.pop() # buggy!

    def size(self) -> int:
        """Get the number of items in the stack"""
        return len(self._items)