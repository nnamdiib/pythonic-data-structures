from treenode.node import Node
from collections import deque
import random

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

  def __len__(self):
    return self.size

  def __iter__(self):
    return self.traverse()

  def __bool__(self):
    return self.size != 0

  def delete(self, node):
    ## Check if tree is empty
    if not self:
      raise ValueError("Cannot Delete from empty tree")

    ## Case #1 -> node to be deleted has no children.
    if node.isleaf():
      if node == self.root:
        self.root = None
      elif node == node.parent.left:
        node.parent.left = None
      else:
        node.parent.right = None
      self.size -= 1

    ## Case #2 -> node to be deleted has exactly 1 child
    #  XOR, baby.
    elif bool(node.left) ^ bool(node.right):
      subtree = node.left if node.left else node.right
      if node == self.root:
        self.root = subtree
        node.left = node.right = None
      elif node == node.parent.left:
        node.parent.left = subtree
      else:
        node.parent.right = subtree
      self.size -= 1

    ## Case #3 -> node to be deleted has 2 children :(
    else:
      right_subtree_min = self.minnode(node.right)
      if node == self.root:
        self.root.data = right_subtree_min.data
      node.data = right_subtree_min.data
      self.delete(right_subtree_min)

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

  # Generator function
  def traverse(self, preorder=False, inorder=False, postorder=False):
    levelorder = False
    if not(preorder or inorder or postorder):
      levelorder = True # leveloder traversal is default, if no flag is set.

    if levelorder:
      return self.levelorder(self.root)
    if preorder:
      return self.preorder(self.root)
    elif inorder:
      return self.inorder(self.root)
    elif postorder:
      return self.postorder(self.root)

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

  # Generator function
  def preorder(self, root):
    if root is None:
      return

    yield root
    yield from self.preorder(root.left)
    yield from self.preorder(root.right)

  # Generator function
  def inorder(self, root):
    if root is None:
      return

    yield from self.inorder(root.left)
    yield root
    yield from self.inorder(root.right)

  # Generator function
  def postorder(self, root):
    if not root:
      return

    yield from self.postorder(root.left)
    yield from self.postorder(root.right)
    yield root

  # leaves(self) -> generator
  def leaves(self):
    return (n for n in self.traverse() if n.isleaf())

  def shake(self):
    # Like shaking an apple tree, and waiting for any apple
    # to fall.
    nodes = [node for node in self.traverse()]
    return random.choice(nodes)

  def minnode(self, root=None):
    if not root:
      root = self.root
    while root.left:
      root = root.left
    return root

  def maxnode(self, root=None):
    if not root:
      root = self.root
    while root.right:
      root = root.right
    return root

  # def isempty(self):
  #   return self.size == 0

  def balance():
    pass

  def invert():
    pass