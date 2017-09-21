# Contains the class definition for a general Node structure
# That can be subclassed to create nodes for Stacks, LinkedLists, B-Trees, etc.

class LNode:
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


class BNode:
  left = None
  right = None
  parent = None
  data = None

  def __init__(self, data=None, left=None, right=None, parent=None):
    if data:
      self.data = data
    if left:
      self.left = left
    if right:
      self.right = right
    if parent:
      self.parent = parent

  def isleaf(self):
    return not(self.left or self.right)

  def isroot(self):
    return not self.parent