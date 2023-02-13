import pytest

from stack import Stack

def test_push_v1():
    s = Stack()
    s.push(3)
    assert s._items == [3]
    s.push(7)
    assert s._items == [3, 7]

"""
def test_push_v2():
    s = Stack()
    s.push(3)
    assert s.size() == 1
    assert s.peek() == 3
    s.push(7)
    assert s.size() == 2
    assert s.peek() == 7
"""

