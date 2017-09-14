from linkedlist import LinkedList

iterable = ("my", "name", "is", "nnamdi")
l = LinkedList(iterable, double=True)

for node in l:
	print(node._data)
	# if node._prev:
	# 	print('***',node._prev._data)

print(len(l))

l.inserthead()

for node in l:
	print(node._data)

print(len(l))

k = LinkedList()

k.inserthead("Nnamdi")

print(k._head._data)

