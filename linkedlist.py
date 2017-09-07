from node import Node

class LinkedList:
  _head = None
  _tail = None
  _size = 0

  def __init__(self, iterable=None):
    if iterable:
      pass

  def __iter__(self):
    n = self._head
    while n:
      yield n
      n = n._next

  def __len__(self):
    return self._size

  def __eq__(self, other):
    pass

  def __bool__(self):
    pass

  def inserthead(self, data=None, node=None):
    if data:
      node = Node(data)
      node._next = self._head
      self._head = node
    elif node:
      node._next = self._head
      self._head = node
    else:
      # raise error
      pass

    self._size += 1

  
  def inserttail(self, data=None, node=None):
    if data and node:
      # raise error
    elif data:
      node = Node(data)
      self._tail._next = node
      node._next = None
      self._tail = node
    elif node:
      self._tail._next = node
      node._next = None
      self._tail = node
    else:
      # raise error

    self._size += 1

  def preinsert(self, target_node, a_node):
    # Insert a_node before the target_node in a given linkedlist.
    pass

  def postinsert(self, target_node, a_node):
  # Insert a_node after the target_node in a given linkedlist.
    pass

  def iscycle(self):
    # returns True if a cycle exists in the LinkedList.

  def getnode(pos=None, data=None):
    # both Ifs run if pos and data are not None
    # find more elegant solution.
    n = None
    if pos:
      if 0 <= pos <= self._size:
        # get the ith node.
        n = self._head
        while pos != 0:
          n = n._next
          pos -= 1
      else:
        # raise error(Not enough nodes in linkedlist,pos to high)
        pass

    if data:
      n = self._head
      while n:
        if n._data == data:
          break
        n = n._next

    return n