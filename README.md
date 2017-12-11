# Pythonic Data Structures

As a learning experiment, I am leveraging the rich Python API to create and extend certain existing data structures like Linked Lists and Binary Search Trees.

I want it to be as simple as pythonic as possible.


## Table of Contents

- [Linked List](https://github.com/nnamdiib/pythonic-data-structures#linked-list)
- [Heap](https://github.com/nnamdiib/pythonic-data-structures#heap)
- [Binary Search Tree](https://github.com/nnamdiib/pythonic-data-structures#binary-search-tree)
- [Things I learned](https://github.com/nnamdiib/pythonic-data-structures#things-i-learned)



All tree data structures will inherit from the Tree superclass in tree.py

Linked List
------------

Object creation and inbuilt operations

```python
import LinkedList

iterable = ('this', 'is', 'an', 'example')

list1 = LinkedList(iterable)
list2 = LinkedList(iterable, double=True) # Create a doubly linked list.

print( list1.head, list2.tail ) # print head and tail of singly and doubly linked lists respectively.

size1 = len(list1)
size2 = len(list2)

```

Traversal
Traversal is done using python generator expressions. The __iter__ method is overriden to yield each node in the linked list.

```python
list_nodes = (node for node in list1) # A Genertor object is returned.

for node in list2:
  print(node.data)
```

Heap
--------
Create a min heap or a max heap:
```python
from heap import Heap

items = [4, 1, 2, 8, 0]

max_heap = Heap(items, heap_type='max') # Create a max heap.
min_heap = Heap(items, heap_type='min') # Create a min heap.
another_min_heap = Heap(items) # no heap_type specified, default is 'min'.

len(min_heap) # --> 5

print(max_heap.root)  # --> 8
print(min_heap.root)  # --> 0
```

Extract:
```python
# The extract() method returns the root of the min or max heap.
# The method also deletes the root and performs a bubble_down or sinkdown
# operation to maintain Heap property.

min_heap.extract()
max_heap.extract()

```

If you want to return the root element without deleting it, simply use:
```python
max_heap.root
min_heap.root
```

Insertion and Deletion:
After every insert, the heap performs a bubble-up operation to maintain the heap property.
After every delete, the heap perfomrs a sink-down or bubble-down operation to maintain heap property.
```python
from heap import Heap
h = Heap() # creates a min heap by default

h.insert(100)
h.insert(10)
h.insert(50)
h.insert(0)

print(len(h)) # --> 4
print(h.root) # --> 0

for node in h:
  if node.data == 100:
    h.delete(node)

print(len(h)) # --> 3

```

Traversal:
The Tree superclass contains the levelorder() traversal method which Heap class inherits. The python __iter__
uses levelorder() to visit every node in a Heap object (And indeed, another other subclass or Tree)
```python
# This is the preferred way to iterate over the nodes.
for node in min_heap:
  print(node.data)

# I will discourage you from using this, though its still correct.
for n in max_heap.levelorder():
  print(n.data)
```


Binary Search Tree
-----------------------
The binary search tree is implemented using Node class in treenode.

Traversal
```python
from bst import BST

items = [3, 2, 8]
tree = BST(items)

for node in tree:
  print(node.data)

for node in tree.traverse(inorder=True):
  print(node.data)

for node in tree.traverse(postorder=True):
  print(node.data)

for node in tree.traverse(preorder=True):
  print(node.data)
```

Getting leaves of the tree
```python

tree_leaves = tree.leaves() # Returns a generator object
```

Find minimum or maximum nodes
```python
min_node = tree.minnode()
max_node = tree.maxnode()
```

Insertion and Deletion
```python
tree = Tree( [6, 3, 9] )
len(tree) # --> 3

tree.insert(100)
len(tree) # --> 4

root_node = tree.root

tree.delete(root_node)

len(tree) # --> 3

```

Things I learned
---------------------
- Object-oriented implementations of data structures such as these would have been easier using a language like C++.
- Python has a weird way of declaring private properties and methods. I avoied it entirely.
- A language like C++ would have simplified this private vs public issue.
- Implementing code to balance a binary search tree is not as easy as I thought!
- OOP is cool cos it can easily model real world objects. Etc. Every MinHeap is a Heap, and every heap is just a special Tree.
  So one can create a MinHeap class that inherits from Heap, which in turn inherits from a Tree class. Neat!
  
## Authors

* **Ibeanusi Nnamdi** - [github](https://github.com/nnamdiib)

## License

This project is licensed under the MIT License
