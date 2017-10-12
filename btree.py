from treenode.node import Node

class Tree:
  height = 0
  size = 0
  root = None
  leaves = []
  visitednodes = []

  def __init__(self, iterable=None):
    if iterable is None:
      iterable = []
    else:
      iterable = list(iterable)

    for v in iterable:
      self.insert(Node(data=v))

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
      print("I inserted Node(%d)"% node.data)
    elif node.data < parent.data:
      parent.left = node
      print("I inserted Node(%d)"% node.data)
    else:
      parent.right = node
      print("I inserted Node(%d)"% node.data)

  def leaves(self):
    pass

  def shake():
    pass

  def getnode():
    pass

  def minnode():
    pass

  def maxnode():
    pass

  def traverse(self,preorder=False, inorder=False, postorder=False):
    self.visitednodes = []
    if preorder:
      self.preorder(self.root)
    elif inorder:
      self.inorder(self.root)
    elif postorder:
      self.postorder(self.root)

    return (node for node in self.visitednodes)



  def preorder():
    pass

  def inorder(self, root):
    if root is None:
      return

    self.inorder(root.left)
    self.visitednodes.append(root)
    self.inorder(root.right)

  def postorder():
    pass


  def balance():
    pass

  def delete():
    pass

  def invert():
    pass