from linkedlist import LinkedList
from btree import Tree
#from listnode.node import Node
from treenode.node import Node

# iterable = ('my', 'name', 'is', 'nnamdi')
# h = [[1,2,3], 6]
# l=LinkedList(h)
# print(l)

iterable = [1,7,3,2,5,8,9,4]
b = Tree()
c = Tree(iterable)

print(c.root.data)

n = (Node(v) for v in [100,5,2,3,1,8])
for x in n:
  b.insert(x)

g = [v.data for v in b.traverse(inorder=True)]
print(g)


# class TestLinkedList:
#   singly = LinkedList(iterable)
#   doubly = LinkedList(iterable, double=True)

#   def test_init():
#     pass

#   def test_iter():
#     pass

#   def test_len():
#     pass

#   def test_eq():
#     pass

#   def test_bool():
#     pass

#   def test_isempty():
#     pass

#   def test_inserthead():
#     pass

#   def test_inserttail():
#     pass

#   def test_preinsert():
#     pass

#   def test_postinsert():
#     pass

#   def test_iscycle():
#     pass

#   def test_getnode():
#     pass