from treenode.node import Node

class Heap:
  root = None
  size = 0
  min_ = False
  max_ = False

  def __init__(self, iterable=None, type='max'):
    if iterable:
      for item in iterable:
        self.insert(item)

  def __len__(self):
    return self.size

  def extract(self):
    return self.root-0

  def insert(self, item):
    pass

  def bubble_up(self, node):
    if self.min_:
      while node.data < node.parent.data:
        temp = node.data
        node.data = node.parent.data
        node.parent.data = temp
    elif self.max_:
      while node.data > node.parent.data:
        temp = node.data
        node.data = node.parent.data
        node.parent.data = temp

  def delete(self, item):
    pass

  def bubble_down(self, item):
    pass

  def get_available_spot(self):
    for node in self.levelorder():
      if node.left ^ node.right:
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