# Contains the class definition for a general Node structure
# That can be subclassed to create nodes for Stacks, LinkedLists, B-Trees, etc.

class Node:
  _next = None
  _prev = None
  _data = None

  def __init__(self, _next=None, prev=None, data=None):
    if _next:
      self._next = _next
    if prev:
      self._prev = prev
    if data:
      self._data = data