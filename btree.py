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
      #print("I inserted Node(%d)"% node.data)
    elif node.data < parent.data:
      parent.left = node
      #print("I inserted Node(%d)"% node.data)
    else:
      parent.right = node
      #print("I inserted Node(%d)"% node.data)

  def traverse(self, preorder=False, inorder=False, postorder=False):
    self.visitednodes = []
    if not(preorder or inorder or postorder):
      inorder = True

    if preorder:
      self.preorder(self.root)
    elif inorder:
      self.inorder(self.root)
    elif postorder:
      self.postorder(self.root)

    return iter(self.visitednodes)

  def preorder(self, root):
    if root is None:
      return

    self.visitednodes.append(root)
    self.preorder(root.left)
    self.preorder(root.right)

  def inorder(self, root):
    if root is None:
      return

    self.inorder(root.left)
    self.visitednodes.append(root)
    self.inorder(root.right)

  def postorder(self, root):
    if not root:
      return

    self.postorder(root.left)
    self.postorder(root.right)
    self.visitednodes.append(root)

  def leaves(self):
    for node in self.traverse():
      if not(node.left or node.right):
        yield node

  def shake():
    pass

  def getnode():
    pass

  def minnode():
    pass

  def maxnode():
    pass


  def balance():
    pass

  def delete():
    pass

  def invert():
    pass