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

#### Object creation and inbuilt operations

```
import LinkedList

iterable = ('this', 'is', 'an', 'example')

list1 = LinkedList(iterable)
list2 = LinkedList(iterable, double=True) # Create a doubly linked list.

print( list1.head, list2.tail ) # print head and tail of singly and doubly linked lists respectively.

size1 = len(list1)
size2 = len(list2)

```

#### Traversal Methods
Traversal is done using pythonic generator expressions. The __iter__ method is overriden to yield each node in the linked list.

```
list_nodes = (node for node in list1) # A Genertor object is returned.

for node in list2:
  print(node.data)
```

## Authors

* **Ibeanusi Nnamdi** - [github](https://github.com/nnamdiib)

## License

This project is licensed under the MIT License
