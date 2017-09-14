from linkedlist import LinkedList

iterable = ("my", "name", "is", "nnamdi")
l = LinkedList(iterable, double=True)

l.inserttail("Ibeanusi")

print(l.tail.data)
print(l.head.data)