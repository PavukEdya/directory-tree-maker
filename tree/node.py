from sortedcontainers import SortedSet


class Node:

    def __init__(self, name, size=None):
        self._name = name
        self._size = size
        self._children = SortedSet(key=self._node_compare)

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def children(self):
        return self._children

    def _node_compare(self, node):
        if node.size is None:
            return (0, node.name)
        else:
            return (1, -node.size, node.name)

    def __str__(self):
        return self._name
