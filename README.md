# Pythonic Data Structures

As a learning experiment, I am leveraging the rich Python API to create and extend certain existing data structures like Linked Lists, Stacks and B-trees.

I want it to be as simple as pythonic as possible, and support operations like

```
import LinkedList
import Stack

iterable = ('this', 'is', 'an', 'example')

singly = LinkedList(iterable)
doubly = LinkedList(iterable, double=True) # Create a doubly linked list.
```

Also,  the data structures will be behave like native python objects. Therefore they will respond to methods like len() or iter().
```
size = len(singly)
print(size)

# They should support iteration like any native python iterable
for node in doubly:
  print(node.data)
```

## Authors

* **Ibeanusi Nnamdi** - [github](https://github.com/nnamdiib)

## License

This project is licensed under the MIT License
