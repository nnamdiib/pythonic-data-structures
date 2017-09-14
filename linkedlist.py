from node import Node

class LinkedList:
  _head = None
  _tail = None
  _size = 0
  _double = False

  def __init__(self, iterable=None, double=False):
    self._double = double
    if iterable:
      left = right = None
      nodes = (Node(item) for item in iterable)
      for n in nodes:
        self._head = n if self.isempty() else self._head
        right = n
        if left:
          left._next = right
        if self._double:
          right._prev = left
        left = right
        self._size += 1
      self._tail = n

  def __iter__(self):
    n = self._head
    while n:
      yield n
      n = n._next

  def __len__(self):
    return self._size

  def __eq__(self, other):
    if len(self) != len(other):
      return False
    for n1, n2 in zip(self, other):
      if n1 != n2:
        return False
    return True

  def __bool__(self):
    return not(self._head == None)

  def isempty(self):
    return self._size == 0

  def inserthead(self, data=None, node=None):
    if data:
      node = Node(data)
      node._next = self._head
      self._head = node
    elif node:
      node._next = self._head
      self._head = node
    else:
      raise TypeError("Provide either the data value or the Node object")

    self._size += 1
  
  def inserttail(self, data=None, node=None):
    if self._size == 0:
      n = Node(data)
      self._tail = self._head = n
    else:
      if data:
        node = Node(data)
        self._tail._next = node
        node._next = None
        if self._double:
          node._prev = self._tail
        self._tail = node
      elif node:
        self._tail._next = node
        node._next = None
        if self._double:
          node._prev = self._tail
        self._tail = node
      else:
        raise TypeError("Provide either the data value or the Node object")
    self._size += 1

  def preinsert(self, target_node, a_node):
    # Insert a_node before the target_node in a given linkedlist.
    pass

  def postinsert(self, target_node, a_node):
  # Insert a_node after the target_node in a given linkedlist.
    pass

  def iscycle(self):
    # returns True if a cycle exists in the LinkedList.
    if self.isempty():
      return False

    h1 = h2 = self._head
    
    while h1 and h2:
      h1 = self._next
      h2 = self._next._next

      if h1 == h2:
        return True

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