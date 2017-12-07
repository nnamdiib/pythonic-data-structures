from treenode.node import Node
from collections import deque

class Heap:
  root = None
  size = 0
  min_ = False
  max_ = False

  def __init__(self, iterable=None, heap_type='min'):
    if heap_type == 'max':
      self.max_ = True
    elif heap_type == 'min':
      self.min_ = True
    else:
      # Raise an error of incorrect param
      pass
    if iterable:
      for item in iterable:
        self.insert(item)

  def __len__(self):
    return self.size

  def __iter__(self):
    return self.levelorder(self.root)

  def extract(self):
    if self.isempty():
      return self.root
    else:
      root = self.root
      self.delete(self.root)
      return root

  def insert(self, item):
    node = Node(item)
    if self.size == 0:
      self.root = node
    else:
      node_with_1_child = self.get_available_spot()
      if not node_with_1_child.left:
        node_with_1_child.left = node
      else:
        node_with_1_child.right = node
      node.parent = node_with_1_child
    self.size += 1 # Increase size before you bubble up!
    self.bubble_up(node)

  def bubble_up(self, node):
    if len(self) < 2:
      return

    # The while conditions below exploit python's Lazy evaluation principle
    # Is there a better way to implement this method
    # without relying on a language implementation detail?
    if self.min_:
      while (node.parent) and (node.data < node.parent.data):
        temp = node.data
        node.data = node.parent.data
        node.parent.data = temp
        node = node.parent
    elif self.max_:
      while (node.parent) and (node.data > node.parent.data):
        temp = node.data
        node.data = node.parent.data
        node.parent.data = temp
        node = node.parent

  def delete(self, node):
    if len(self) < 2:
      return
    bottom_node = list(self.leaves())[-1]
    node.data = replace_node.data
    if bottom_node.parent.left == bottom_node:
      bottom_node.parent.left = None
    else:
      bottom_node.parent.right = None
    bottom_node.parent = None
    self.size -= 1
    bubble_down(node)

  def bubble_down(self, item):
    pass

  def get_available_spot(self):
    for node in self:
      if not(node.left and node.right):
        return node

  # Generator function
  def levelorder(self, root):
    q = deque()
    if root:
      q.append(root)
    while len(q) != 0:
      front = q.popleft()
      yield front
      if front.left:
        q.append(front.left)
      if front.right:
        q.append(front.right)

  def leaves(self):
    return (n for n in self if n.isleaf())

  def isempty(self):
    return self.size == 0