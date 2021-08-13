from typing import TypeVar


_ND = TypeVar('_ND')

class Node:
    def __init__(self, name: str, neighbors: _ND = None) -> None:
        self.name = name
        self.neighbors = dict()
        if neighbors is not None:
            for n in neighbors:
                self.add_neighbor(n, neighbors[n])

    def __repr__(self):
        return f'{self.name}: {[f"{n.name}:{self.neighbors[n]}" for n in self.neighbors]}'

    def add_neighbor(self, o, dist: int) -> None:
        if o is not None:
            self.neighbors[o] = dist
            o.neighbors[self] = dist

    def add_neighbors(self, neighbors: _ND) -> None:
        if neighbors is not None:
            for n in neighbors:
                self.add_neighbor(n, neighbors[n])

_ND.__constraints__ = (dict, Node)
_NL = TypeVar('_NL', list, Node)


class Graph:
    def __init__(self, *nodes) -> None:
        if isinstance(nodes[0], list) or isinstance(nodes[0], tuple):
             self.nodes = set(nodes[0].copy())
        else:
            self.nodes = set()
            for n in nodes:
                self.nodes.add(n)
    
    def add_edge(self, vs: Node, ve: Node, dist: int):
        self.nodes.add(vs)
        self.nodes.add(ve)
        vs.add_neighbor(ve, dist)

    def add_neighbors(self, root:Node, neighbors: _ND = None):
        self.nodes.add(root)
        [self.add_node(n) for n in neighbors]
        root.add_neighbors(neighbors)
    
    def add_node(self, o: Node):
        self.nodes.add(o)

    def __repr__(self):
        return '\n'.join([str(n) for n in self.nodes])


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')

    g = Graph(a, b, c, d, e)
    g.add_neighbors(a, {b: 1, d: 2, c:2, e:1})
    g.add_neighbors(b, {a: 1, c:4})
    g.add_neighbors(c, {b: 4, a:2, e: 5})
    g.add_neighbors(e, {c: 5, a: 1, d: 3})
    g.add_neighbors(d, {a:2, e:3})
    print(g)
