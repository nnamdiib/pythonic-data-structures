# Node for Linked List
class Node:
  next = None
  prev = None
  data = None

  def __init__(self, data=None, next=None, prev=None):
    if next:
      self.next = next
    if prev:
      self.prev = prev
    if data:
      self.data = data

  def __eq__(self, other):
    equal = True
    if self.next or other.next:
      equal = equal and (self.next is other.next)
    if self.prev or other.prev:
      equal = equal and (self.prev is other.prev)
    if self.data or other.data:
      equal = equal and (self.data is other.data)
    return equal