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
    if len(self) > 1:
      if self.min_:
        while node.data < node.parent.data:
          print("Node 1:", node.data)
          print("Node 2:", node.data)
          temp = node.data
          node.data = node.parent.data
          node.parent.data = temp
          node = node.parent
      elif self.max_:
        while node.data > node.parent.data:
          temp = node.data
          node.data = node.parent.data
          node.parent.data = temp
          node = node.parent

  def delete(self, item):
    pass

  def bubble_down(self, item):
    pass

  def get_available_spot(self):
    for node in self.levelorder():
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
    return (n for n in self.levelorder(root) if n.isleaf())

  def isempty(self):
    return self.size == 0