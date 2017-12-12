from treenode.node import Node
from collections import deque
from tree import Tree

class Heap(Tree):
  MIN = False
  MAX = False

  def __init__(self, iterable=None, heap_type='min'):
    if heap_type == 'max':
      self.MAX = True
    elif heap_type == 'min':
      self.MIN = True
    else:
      raise ValueError("Heap type must be either 'min' or 'max' ")
    if iterable:
      for item in iterable:
        self.insert(item)

  def __str__(self):
    heap_type = '[Min Heap]' if self.MIN else '[Max Heap]'
    description = '%s with %d elements.' %(heap_type, len(self))
    return description

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

  def delete(self, node):
    if self.isempty():
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

  def get_available_spot(self):
    for node in self:
      if not(node.left and node.right):
        return node

  def swapnodes(self, node1, node2):
    temp = node1.data
    node1.data = node2.data
    node2.data = temp

class MaxHeap(Heap):
  heap_size = None
  def __init__(self, iterable=None, heap_size=None):
    if heap_size:
      self.heap_size = heap_size
    self = super().__init__(iterable, heap_type='max')

  def bubble_up(self, node):
    if len(self) < 2:
      return
    # The while conditions below exploit python's Lazy evaluation principle
    # Is there a better way to implement this method
    # without relying on a language implementation detail?
    while (node.parent) and (node.data > node.parent.data):
      self.swapnodes(node, node.parent)
      node = node.parent

  def bubble_down(self, node):
    if len(self) < 2:
      return
    # The while conditions below exploit python's Lazy evaluation principle
    # Is there a better way to implement this method
    # without relying on a language implementation detail?
    while (node.left and node.left.data > node.data) or (node.right and node.right.data > node.data):
      replacer = node.left if node.left.data > node.right.data else node.right
      self.swapnodes(node, replacer)
      if replacer == node.left:
        node = node.left
      else:
        node = node.right


class MinHeap(Heap):
  heap_size = None
  def __init__(self, iterable=None, heap_size=None):
    if heap_size:
      self.heap_size = heap_size
    self = super().__init__(iterable, heap_type='min')

  def bubble_up(self, node):
    if len(self) < 2:
      return
    # The while conditions below exploit python's Lazy evaluation principle
    # Is there a better way to implement this method
    # without relying on a language implementation detail?
    while (node.parent) and (node.data < node.parent.data):
      self.swapnodes(node, node.parent)
      node = node.parent

  def bubble_down(self, node):
    if len(self) < 2:
      return
    # The while conditions below exploit python's Lazy evaluation principle
    # Is there a better way to implement this method
    # without relying on a language implementation detail?
    while (node.left and node.left.data < node.data) or (node.right and node.right.data < node.data):
      replacer = node.left if node.left.data < node.right.data else node.right
      self.swapnodes(node, replacer)
      if replacer == node.left:
        node = node.left
      else:
        node = node.right