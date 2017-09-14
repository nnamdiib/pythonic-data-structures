from node import Node

class LinkedList:
  head = None
  tail = None
  size = 0
  double = False

  def __init__(self, iterable=None, double=False):
    self.double = double
    if iterable:
      left = right = None
      nodes = (Node(item) for item in iterable)
      for n in nodes:
        self.head = n if self.isempty() else self.head
        right = n
        if left:
          left.next = right
        if self.double:
          right.prev = left
        left = right
        self.size += 1
      self.tail = n

  def __iter__(self):
    n = self.head
    while n:
      yield n
      n = n.next

  def __len__(self):
    return self.size

  def __eq__(self, other):
    if len(self) != len(other):
      return False
    for n1, n2 in zip(self, other):
      if n1 != n2:
        return False
    return True

  def __bool__(self):
    return not(self.head == None)

  def isempty(self):
    return self.size == 0

  def inserthead(self, data=None, node=None):
    if data:
      node = Node(data)
      node.next = self.head
      self.head = node
    elif node:
      node.next = self.head
      self.head = node
    else:
      raise TypeError("Provide either the data value or the Node object")

    self.size += 1
  
  def inserttail(self, data=None, node=None):
    if self.size == 0:
      n = Node(data)
      self.tail = self.head = n
    else:
      if data:
        node = Node(data)
        self.tail.next = node
        node.next = None
        if self.double:
          node.prev = self.tail
        self.tail = node
      elif node:
        self.tail.next = node
        node.next = None
        if self.double:
          node.prev = self.tail
        self.tail = node
      else:
        raise TypeError("Provide either the data value or the Node object")
    self.size += 1

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

    h1 = h2 = self.head
    
    while h1 and h2:
      h1 = self.next
      h2 = self.next.next

      if h1 == h2:
        return True

  def getnode(pos=None, data=None):
    # both Ifs run if pos and data are not None
    # find more elegant solution.
    n = None
    if pos:
      if 0 <= pos <= self.size:
        # get the ith node.
        n = self.head
        while pos != 0:
          n = n.next
          pos -= 1
      else:
        # raise error(Not enough nodes in linkedlist,pos to high)
        pass

    if data:
      n = self.head
      while n:
        if n.data == data:
          break
        n = n.next

    return n