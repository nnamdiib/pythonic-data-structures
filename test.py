from linkedlist import LinkedList
from node import Node

iterable = ("my", "name", "is", "nnamdi")
l = LinkedList(iterable)

l.inserttail("Ibeanusi")
c = None
for n in l:
	if n.data == "name":
		c=n
		break


i = Node("tags")
j = Node("Full")
l.postinsert(n, i )

for n in l:
	print(n.data)

h = l.getnode(2)
l.preinsert(5, j)
print("*"*10)

for n in l:
	print(n.data)


