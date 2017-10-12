from node import Bnode

class Tree:
  height = 0
  size = 0
  root = None
  leaves = []

  def __init__(iterable=None, root=None):
    if root and iterable:
      assert(root in iterable)
    elif root:
      # delete the root from the iterable
      iterable.find(root)
    elif iterable:
      # default root is the first item
      root = iterable[0]


  def __len__():
    pass

  def __iter__():
    pass

  def __str__():
    pass

  def insert(self, node):
    n = self.root
    while n:
      y = n
      if node.data < n.data:
        n = n.left
      else:
        n = n.right
    node.parent = y
    if not y:
      self.root = node
    elif node.data < y.data:
      y.left = node
    else:
      y.right = node

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