from treenode.node import Node

class Tree:
  height = 0
  size = 0
  root = None
  leaves = []

  def __init__(self, iterable=None, root=None):
    if iterable is None:
      iterable = []
    else:
      iterable = list(iterable)
    if root and iterable:
      assert(root in iterable)
      self.insert(Node(root))
      del iterable[ iterable.index(root) ]
    elif root:
      self.insert(Node(root))
    elif iterable:
      # default root is the first item
      root = iterable[0]
      self.insert(Node(root))
      del iterable[0]
      for v in iterable:
        self.insert(Node(v))


  # def __len__():
  #   pass

  # def __iter__():
  #   pass

  # def __str__():
  #   pass

  def insert(self, node):
    n = self.root
    parent = None
    while n:
      parent = n
      if node.data < n.data:
        n = n.left
      else:
        n = n.right
    node.parent = parent
    if not parent:
      self.root = node
    elif node.data < parent.data:
      parent.left = node
    else:
      parent.right = node

  def shake():
    pass

  def getnode():
    pass

  def minnode():
    pass

  def maxnode():
    pass

  def preorder():
    pass

  def inorder():
    pass

  def postorder():
    pass


  def balance():
    pass

  def delete():
    pass

  def invert():
    pass