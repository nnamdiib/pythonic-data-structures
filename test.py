from linkedlist import LinkedList
from node import LNode

iterable = ('my', 'name', 'is', 'nnamdi')
h = [[1,2,3], 6]
l=LinkedList(h)
print(l)

class TestLinkedList:
  singly = LinkedList(iterable)
  doubly = LinkedList(iterable, double=True)

  def test_init():
    pass

  def test_iter():
    pass

  def test_len():
    pass

  def test_eq():
    pass

  def test_bool():
    pass

  def test_isempty():
    pass

  def test_inserthead():
    pass

  def test_inserttail():
    pass

  def test_preinsert():
    pass

  def test_postinsert():
    pass

  def test_iscycle():
    pass

  def test_getnode():
    pass