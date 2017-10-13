# Node for Binary Trees
class Node:
  left = None
  right = None
  parent = None
  data = None

  def __init__(self, data=None, left=None, right=None, parent=None):
    self.data = data
    self.left = left
    self.right = right
    self.parent = parent

  def isleaf(self):
    return not(self.left or self.right)

  def isroot(self):
    return not self.parent