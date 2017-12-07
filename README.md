# Pythonic Data Structures

As a learning experiment, I am leveraging the rich Python API to create and extend certain existing data structures like Linked Lists and Binary Search Trees.

I want it to be as simple as pythonic as possible.


## Table of Contents

- [Linked List](https://github.com/nnamdiib/pythonic-data-structures#linked-list)
- [Heap](https://github.com/nnamdiib/pythonic-data-structures#heap)
- [Binary Search Tree](https://github.com/nnamdiib/pythonic-data-structures#binary-search-tree)


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
## Authors

* **Ibeanusi Nnamdi** - [github](https://github.com/nnamdiib)

## License

This project is licensed under the MIT License
