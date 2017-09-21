class Tree:
  height = 0
  size = 0
  root = None
  leaves = []

  def __init__():
    pass

  def __len__():
    pass

  def __iter__():
    pass

  def __str__():
    pass

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

  def balance():
    pass

  def delete():
    pass

  def invert():
    pass