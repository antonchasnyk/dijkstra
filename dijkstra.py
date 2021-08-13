from min_heap import MinHeap
from simple_graph import Graph, Node
from math import inf

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")

graph = Graph()
graph.add_neighbors(a, {b: 1, c: 3})
graph.add_neighbors(b, {a: 1, c: 1})
graph.add_neighbors(c, {e: 4, f: 2, d: 1})
graph.add_neighbors(e, {f: 1})
graph.add_neighbors(d, {f: 3})
graph.add_neighbors(f, {h: 4, g: 5, i: 3})
graph.add_neighbors(i, {h: 2, g: 7})

mh = MinHeap()
for n in graph.nodes:
    mh[n] = inf, None
mh[a] = 0, None

current, summ = mh.pop()
visited = set([current])
print(f"{current.name}: {summ} hops form A")
while mh.is_not_empty():
    unvisited = set(current.neighbors) - visited
    for n in unvisited:
        val = summ[0] + current.neighbors[n]
        mh[n] = val, current
    current, summ = mh.pop()
    visited.add(current)
    print(
        f"{current.name}: {summ[0]} hops form A. "
        f"Parent vertice {summ[1].name}"
    )
