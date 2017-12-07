from treenode.node import Node
from collections import deque
from tree import Tree

class Heap(Tree):
  MIN = False
  MAX = False

  def __init__(self, iterable=None, heap_type='min', max_size=None):
    if heap_type == 'max':
      self.MAX = True
    elif heap_type == 'min':
      self.MIN = True
    else:
      raise ValueError("Heap type must be either 'min' or 'max' ")
    if iterable:
      for item in iterable:
        self.insert(item)

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
    if self.MIN:
      while (node.parent) and (node.data < node.parent.data):
        temp = node.data
        node.data = node.parent.data
        node.parent.data = temp
        node = node.parent
    elif self.MAX:
      while (node.parent) and (node.data > node.parent.data):
        temp = node.data
        node.data = node.parent.data
        node.parent.data = temp
        node = node.parent

  def delete(self, node):
    if len(self) < 2:
      return

    bottom_node = list(self.leaves())[-1]
    node.data = bottom_node.data

    if bottom_node.parent.left == bottom_node:
      bottom_node.parent.left = None
    else:
      bottom_node.parent.right = None

    bottom_node.parent = None
    self.size -= 1

    self.bubble_down(node)

  def bubble_down(self, node):
    if len(self) < 2:
      return

    # The while conditions below exploit python's Lazy evaluation principle
    # Is there a better way to implement this method
    # without relying on a language implementation detail?
    if self.MIN:
      while (node.left and node.left.data < node.data) or (node.right and node.right.data < node.data):
        replacer = node.left if node.left.data < node.right.data else node.right
        temp = node.data
        node.data = replacer.data
        replacer.data = temp
        if replacer == node.left:
          node = node.left
        else:
          node = node.right
    elif self.MAX:
      while (node.left and node.left.data > node.data) or (node.right and node.right.data > node.data):
        replacer = node.left if node.left.data > node.right.data else node.right
        temp = node.data
        node.data = replacer.data
        replacer.data = temp
        if replacer == node.left:
          node = node.left
        else:
          node = node.right

  def get_available_spot(self):
    for node in self:
      if not(node.left and node.right):
        return node