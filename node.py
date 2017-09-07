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

  def __eq__(self, other):
    equal = True
    if self._next or other._next:
      equal = equal and (self._next == other._next)
    if self._prev or other._prev:
      equal = equal and (self._prev == other._prev)
    if self._data or other._data:
      equal = equal and (self._data == other._data)
    return equal