class Tree:
  root = None
  size = 0

  def __init__(self):
    pass

  def __len__(self):
    return self.size

  def __iter__(self):
    return self.levelorder(self.root)
    
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

  def leaves(self):
    return (n for n in self if n.isleaf())

  def isempty(self):
    return self.size == 0