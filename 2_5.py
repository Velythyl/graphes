import igraph
from igraph import Graph

def gen_cay(id):
    g = Graph()

    g.add_vertices(6)

    if id != 1:
        for i in range(6):
            g.add_edge(i,(i+1) % 6)
    else:
        for i in range(5):
            g.add_edge(i,i+1 % 6)

    if id != 2:
        g.add_edge(0,2)
    g.add_edge(2,4)
    g.add_edge(4,0)

    g.add_edge(1,3)
    g.add_edge(3,5)
    g.add_edge(5,1)

    return g

g1 = gen_cay(1)
g2 = gen_cay(2)

print(g1)
print(g2)

print(g1.isomorphic(g2))