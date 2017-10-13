from linkedlist import LinkedList
from btree import Tree
#from listnode.node import Node
from treenode.node import Node

# iterable = ('my', 'name', 'is', 'nnamdi')
# h = [[1,2,3], 6]
# l=LinkedList(h)
# print(l)

# iterable = [1,7,3,2,5,8,9,4]
d = Tree()
f = Tree()

# print(c.root.data)

n = (Node(v) for v in [100,5,2,3,1,8])
for x in n:
  f.insert(x)

# g = [v.data for v in b.traverse(postorder=True)]
# print(g)

nodes = [Node(data=x) for x in (2,1,3)]
a,b,c = nodes

d.insert(a)
d.insert(b)
d.insert(c)

d.traverse(preorder=True)
d.traverse(postorder=True)
# print([g.data for g in d.traverse()])
# print([g.data for g in d.traverse(preorder=True)])
# print([g.data for g in d.traverse(postorder=True)])

# print([g.data for g in f.traverse()])
# print([g.data for g in f.traverse(preorder=True)])
# print([g.data for g in f.traverse(postorder=True)])

# print(list(g.data for g in f.leaves()))

for n in f:
  print(n.data)

print(len(f))

