from linkedlist import LinkedList

iterable = ("my", "name", "is", "nnamdi")
l = LinkedList(iterable, double=True)

l.inserttail("Ibeanusi")

print(l._tail._data)
print(l._head._data)