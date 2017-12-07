# Pythonic Data Structures

As a learning experiment, I am leveraging the rich Python API to create and extend certain existing data structures like Linked Lists and Binary Search Trees.

I want it to be as simple as pythonic as possible.


## Table of Contents

- [Linked Lists](https://github.com/nnamdiib/pythonic-data-structures#linked-list)
- [Classic Algorithms](https://github.com/karan/Projects#classic-algorithms)
- [Graph](https://github.com/karan/Projects#graph)
- [Data Structures](https://github.com/karan/Projects#data-structures)
- [Text](https://github.com/karan/Projects#text)
- [Networking](https://github.com/karan/Projects#networking)
- [Classes](https://github.com/karan/Projects#classes)
- [Threading](https://github.com/karan/Projects#threading)
- [Web](https://github.com/karan/Projects#web)
- [Files](https://github.com/karan/Projects#files)
- [Databases](https://github.com/karan/Projects#databases)
- [Graphics and Multimedia](https://github.com/karan/Projects#graphics-and-multimedia)
- [Security](https://github.com/karan/Projects#security)


All tree data structures will inherit from the Tree superclass in tree.py

LinkedLists
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
