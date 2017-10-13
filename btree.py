from treenode.node import Node

class Tree:
  root = None
  size = 0

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
    elif node.data < parent.data:
      parent.left = node
    else:
      parent.right = node

    self.size += 1

  def traverse(self, preorder=False, inorder=False, postorder=False):
    if not(preorder or inorder or postorder):
      inorder = True

    if preorder:
      return self.preorder(self.root)
    elif inorder:
      return self.inorder(self.root)
    elif postorder:
      return self.postorder(self.root)


  def preorder(self, root):
    if root is None:
      return

    yield root
    yield from self.preorder(root.left)
    yield from self.preorder(root.right)

  def inorder(self, root):
    if root is None:
      return

    yield from self.inorder(root.left)
    yield root
    yield from self.inorder(root.right)

  def postorder(self, root):
    if not root:
      return

    yield from self.postorder(root.left)
    yield from self.postorder(root.right)
    yield root

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