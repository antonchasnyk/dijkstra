from min_heap import MinHeap
from simple_graph import Graph, Node
from math import inf

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

g = Graph(a, b, c, d, e)
g.add_neighbors(a, {b: 1, d: 2, c:4, e:1})
g.add_neighbors(b, {a: 1, c:1})
g.add_neighbors(c, {b: 1, a:4, e: 5})
g.add_neighbors(e, {c: 5, a: 1, d: 3})
g.add_neighbors(d, {a:2, e:3})

mh = MinHeap()
for n in g.nodes:
    mh[n] = inf
mh[a] = 0

current, summ = mh.pop()
visited = set([current])
print(f'{current.name}: {summ} hops form A')
while mh.is_not_empty():
    unvisited = set(current.neighbors) - visited
    for n in unvisited:
        mh[n] = summ + current.neighbors[n]
    current, summ = mh.pop()
    visited.add(current)
    print(f'{current.name}: {summ} hops form A')